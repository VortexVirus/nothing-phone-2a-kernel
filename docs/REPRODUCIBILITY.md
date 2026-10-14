# Reproducibility and provenance

Source pins, dependency commits and original artifact hashes are stored in manifests/. The chosen final GKI source is 90700ba133db2fb1d2b05519d45de38ad3d148e1; installed FPSGO source is 313c21a9dc2358667e9640e35738d2e9cab49a5e. The manifest's old SUSFS status string is historical and superseded by STATUS.md and actual build evidence.

Historical stock pipeline-01 and repro-02 were documented as byte-identical for kernel/modules using the same fixed signing key. That claim concerns those stock builds, not a newly repeated custom build here. Historical repeated packaging also produced identical images with the same inputs/key; it was not a second independent compilation.

For equivalent compilation, pin source snapshots, config, clang, build tools, sysroot, epoch 1746772579, anonymous build-user/build-host/version 1, architecture, LTO/CFI/KMI settings, input paths and module selection. KernelSU historical port contains 3296 commits, producing version 33296; the export sets that value directly because private Git history is absent. kernel/.scmversion pins a distinct export suffix. Patch manifests distinguish export changes from recovered development.

Exact historical binary reproduction is not promised: the private signing keys are excluded, the final config contained an absolute build whitelist path, DWARF paths and SCM suffix differ, and module signatures/new random keys change bytes. Source patches and sanitized logs also have different hashes from originals. Do not reinterpret historical SHA256SUMS as checksums of redacted metadata. CONTENTS.sha256 in each final archive hashes the delivered files; historical-artifact-verification.json describes verification against the source project before redaction.

The new isolated archival build is recorded separately in manifests/archive-build.json. Its products are local-only, not device-tested, and must not be mixed with historical OEM/vendor packages. Raw debug files can contain build paths. The original project and original builds were not overwritten.

Fresh dependency retrieval is pinned but depends on continued upstream availability. The complete local archive preserves the locally available toolchain/pipeline with secret test-key files excluded. Public sources retain licenses but exclude opaque prebuilt binaries and some upstream selftest assets; the normal GKI build does not require them. Entire userspace applications and unrelated selftests are not promised to build from that reduced snapshot.

Archive integrity and extraction are tested separately. A scanner cannot prove absence of all sensitive information: unknown identifiers, encoded data, attribution ambiguity and proprietary binary formats remain review limitations. See PRIVACY.md and LICENSES.md before publishing.

The actual archival export release string is `5.15.178-g90700ba133db2`; the historical release was `5.15.178-android13-8-g90700ba133db`. This is recorded explicitly in manifests/new-build-input-checks.json. Do not treat the newly signed export kernel as a drop-in replacement for the historical vendor/package set. Apart from the relocated whitelist path, the generated CONFIG values were identical in the input check.

## Archival rebuild outcome

The independent source-export build completed successfully on 2026-10-13 (exit 0). Image, Image.gz, Image.lz4, vmlinux, symbol metadata and two generic GKI modules were produced. Both compressed images decode exactly to Image. All 8427 exports and CRCs match historical userns-02; actual DWARF dump and ABI comparison returned 0. No compiler warning/error or clock-skew line was found. This validates the host build and inspected interfaces, not a phone installation. The new release string is 5.15.178-g90700ba133db2; signatures and binaries differ from the historical package. No new vendor/package or physical validation was performed. New Image SHA256: af40992e6af896ddde640bfa54393a0eadfea17ab359a87864e60e699d803fc7.
