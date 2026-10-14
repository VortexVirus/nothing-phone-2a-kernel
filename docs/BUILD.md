# Building and recovering the actual pipeline

## Environment and dependencies

Historical environment: Debian 13 x86_64, 40 GiB RAM; Full LTO previously exceeded 20 GiB RSS and sometimes required additional swap. Use local storage for build outputs: NFS clock-skew warnings occurred historically. Reserve roughly 40–80 GiB for a fresh kernel and symbols, more for vendor outputs. Use six jobs initially and measure memory; no swap or host settings are changed by the supplied scripts.

Install Git, Python 3.12+, make, gcc, g++, flex, bison, bc, libssl-dev, libelf-dev, libncurses-dev, dwarves, cpio, openssl, rsync, lz4, zstd, device-tree-compiler, ninja-build, e2fsprogs and erofs-utils. The Android pipeline supplies pinned tools, including pahole 1.23. No full AOSP checkout, JDK or Bazel build is required for this GKI path.

Toolchain: Android clang **r450784e / 8508608 / 14.0.7**, LLVM commit `4c603efb0cca074e9238af8b4106c30add4418f6`. Prebuilt repository commit `9f759dee5cdc5f85d076c642a192f6a9232f7058`; archive SHA256 `af92cdc5f84defd0a754b1d3b3ded9f0da29a737efba5a796c4ebff5a71baa3d`. NDK r23 sysroot commit `93532f3052c14fbb337ff57d5732128dc7481ee6`, archive SHA256 `705ddc9f201a9436c2edf0952f65697d45c9bd788e1375f51b69d004450b777a`. Exact minimal build-tool revisions are in manifests/dependencies.json and the archived Google build 13471816 manifest.

## GKI commands

```sh
python3 scripts/setup-dependencies.py
python3 scripts/build.py --out "$PWD/.work/kernel-01" --dist "$PWD/.work/dist-01" --jobs 6
```

Python downloads exact dependency commits and checks toolchain archive hashes. It refuses an existing dependency checkout at another revision. An existing local pipeline can be supplied with `--pipeline PATH` to both commands. Source tree, pipeline and outputs must have no spaces. The source export already contains the custom changes: do not apply gki-custom.patch again.

The build uses Android build/kernel `b05fb2e75ba86f934da7fbcb4435678a54645c5f`, `build/build.sh`, KERNEL_DIR=common-nomount-userns, gki_defconfig plus KSU and pacman_droidspaces.fragment, SOURCE_DATE_EPOCH=1746772579. Full LTO, CFI, strict KMI and MODVERSIONS remain active. Archive export pins Next version to 33296/v3.4.0 without private Git history. The source suffix in kernel/.scmversion is an export build input and differs from the original generated suffix.

Unlike the historical wrapper, configs/build.config.archive does not copy a private module-signing key. Kbuild generates a new key in the output tree. It also disables generic GKI boot/system_dlkm/certification packaging, leaving Image, compressed Images, vmlinux, symbols and GKI modules as applicable. This is a documented export adaptation, not a new device feature. Outputs and logs are local-only until inspected: DWARF, the embedded config and logs can contain build paths. Do not publish certs/signing_key.pem.

configs/historical-userns-02.config is a reference with its absolute whitelist path normalized; it therefore does not have the original config hash. Kbuild regenerates the whitelist for the current output directory.

## OEM and vendor recovery

Fetch these repositories at exact revisions, not floating heads:

```sh
git init oem-kernel
git -C oem-kernel fetch --depth=1 https://github.com/NothingOSS/android_kernel_5.15_nothing_mt6886.git 02f45fecd3aa6780740aca0a79a120b810f7c744
git -C oem-kernel checkout --detach FETCH_HEAD
git init oem-modules
git -C oem-modules fetch --depth=1 https://github.com/NothingOSS/android_kernel_modules_nothing_mt6886.git 733567edc7c458342db0ad12593821add4a0c7f0
git -C oem-modules checkout --detach FETCH_HEAD
git -C oem-kernel apply ../patches/fpsgo06.patch
```

Adjust the patch path to the export location. Preserve all OEM notices and review rights for precompiled objects. FPSGO07 is a separate optional experiment and is not part of the final installed reference.

The historical vendor sequence is preserved as sanitized source recipes in scripts/historical-recipes/: build-vendor-userns.py (main), vendor-droidspaces-supplement.py (conninfra/WLAN/MSYNC/BT), symbol and type-layout checkers, seal-vendor-userns.py, build-fpsgo06-userns.py, check-fpsgo06-userns.py, compose-userns-fpsgo06.py and package-userns-fpsgo06.py. These templates retain the actual command logic and are **not** a tested turnkey public vendor builder. They expect the historical sources/gki, nothing-vendor-stock, nothing-vendor-perf and nothing-modules-stock layout plus reference artefacts. The complete local archive preserves those inputs and the original sanitized records. Reconstruct the layout and replace PROJECT_ROOT/BUILD_CACHE placeholders before reuse; do not run copied legacy paths against the original project.

Main vendor config: gki_defconfig + mgk_64_k515_defconfig user + DroidSpaces/USER_NS fragment; TARGET_BUILD_VARIANT=user must be explicit. TOP needs both kernel-5.15 and kernel/kernel-5.15 aliases. Build supplementary modules with absolute M paths. Preserve vendor zram/zsmalloc with writeback, not the generic GKI pair. Use generated symbol maps and config from the same new kernel; original signed modules and a newly signed GKI are not assumed compatible.

## Packaging and validation

No ready-to-flash image is produced by the public build. Device packaging requires legally obtained exact OEM boot/vendor_boot/vendor_dlkm/vbmeta/vbmeta_vendor inputs, DTB, ramdisk metadata, module manifests, SELinux labels, AVB rollback indices and corresponding original recovery images. The historical package used a local AVB test key, flags 0 and preserved verity; it is not OEM-signed. Its private key is intentionally unavailable here. Generate independent private keys only in a private workspace, rebuild the entire matching chain and review device acceptance. Do not claim identical signatures.

Verify configs, Image hashes, module selection, ELF imports/exports/CRC, CFI, vermagic and representative layouts. The known optional TUI closure exception must remain explicit. New host build success does not authorize installation or prove hardware support.

## Observed failures

- UID/GID modpost failures: use final six-export KMI list, rebuild GKI and vendor modules.
- Header lookup failures in GPS/DVFSRC: restore both historical TOP aliases.
- Wi-Fi debug imports: ensure TARGET_BUILD_VARIANT=user for main and supplements.
- Wrong linker for SUSFS helper: use -fuse-ld=lld with Android sysroot.
- Wrong ABI reference: abi.xml copied from source is not the new vmlinux DWARF dump.
- NFS timestamp warnings: use local output storage and record timing differences.
- Memory pressure at Full LTO: reduce jobs, inspect available RAM/swap; do not silently change LTO/CFI.

See manifests/archive-build.json for the actual archival compilation outcome, including any remaining blocker. Dependency download over the network and a full new vendor/package rebuild were not inferred from a successful kernel build.
