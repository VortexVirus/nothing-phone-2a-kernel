# Nothing Phone (2a) custom kernel — Pacman

this code is most probably shit as i am in no way capable of checking wtf he did.
this is made by codex after i failed miserably multiple times i still dont know where he got this from and how he did this but as i am in no position to complain, i wont.
this kernel can totaly be taken to make other things to nothing phone 2a i really dont care and dont think anyone else has made a working kernel like this.


**THIS IS VIDE CODED ON SOMETHING I DO NOT KNOW AND UNDERSTAND USE AT YOUR OWN RISK AND DO CHECK BEFORE BLINDLY TRUSTING THIS IS GOOD AND FUNCTIONING**

**you need to use magiskboot to unpack and repack the boot.img for YOUR PACMAN VERSION please check it is the right version get the correct boot.img from https://nothingarchive.tech/**
(the boot.img in this repo is my current version which is : Pacman-B4.0-251230-2052)


Recovered development snapshot for **Nothing Phone (2a), Pacman, MT6886**, targeting Nothing OS **B4.0-251230-2052**. This is not a Phone (3) project. Linux **5.15.178**, based on the exact Google GKI shipped in the target firmware, with separate Nothing vendor sources.

The snapshot integrates KernelSU Next v3.4.0 with a local SUSFS 2.3.0 port, DroidSpaces prerequisite configuration including USER_NS, and NoMount 2.0.0. Vendor FPSGO06 optimizations are supplied as patches. The later FPSGO07 experiment is separate and was not the installed build.

Historical builds and a physical boot are documented. Creating a user namespace was observed; UID/GID root mapping and the latest DroidSpaces sandbox are **not validated**. A previous DroidSpaces container configuration was reported functional by the user. No overall performance gain was established. This archive is prepared for technical and licensing review, not a certified flashable release.

## Build the exported GKI

On x86_64 Debian with Python 3.12+, Git and the packages in [BUILD](docs/BUILD.md):

```sh
python3 scripts/setup-dependencies.py
python3 scripts/build.py --out "$PWD/.work/kernel-01" --dist "$PWD/.work/dist-01" --jobs 6
```

Use a fresh output directory and paths without spaces. The scripts never contact a phone. New signing keys are generated locally and must not be published. The kernel alone is **incompatible with stock vendor modules** for the DroidSpaces configuration. Follow [BUILD](docs/BUILD.md) and [INSTALLATION](docs/INSTALLATION.md) before considering device packaging.

## Contents and evidence

- `kernel/`: recovered final custom GKI source, with documented export-only adjustments.
- `components/`: pinned third-party source snapshots; opaque binaries omitted.
- `patches/`: kernel, KernelSU port, vendor FPSGO06 and separate FPSGO07 differences.
- `configs/`, `scripts/`, `manifests/`: configuration, relocatable GKI build and exact revisions.
- `docs/`: architecture, status, limitations, build and installation prerequisites.
- `release/`: metadata only; no OEM image or unreviewed binary distribution.

Read [STATUS](docs/STATUS.md), [PATCHES](docs/PATCHES.md), [REPRODUCIBILITY](docs/REPRODUCIBILITY.md), [LICENSES](LICENSES.md) and [CREDITS](CREDITS.md). Original copyright notices and component licenses are preserved. The GPL version boundary of integrated components requires clarification before publishing this integrated source snapshot or a combined binary. No private Git history, signing keys or device identifiers are intentionally included.

An independent archival GKI rebuild succeeded, with matching 8427 export CRCs and no ABI difference from the historical final kernel. See manifests/archive-build.json. This does not validate the new binary on a phone.
