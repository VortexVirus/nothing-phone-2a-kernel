# Installation prerequisites and return to original firmware

This is a preparation document, not authorization to flash. No phone was contacted during archival. The public archive has no certified flashable release.

Only Nothing Phone (2a) / Pacman with the exact target firmware B4.0-251230-2052 is covered by the historical evidence. Confirm the live model, firmware, bootloader state, current slot, partition sizes, Virtual A/B snapshot state and recovery access before any future action. A successful getvar command with an empty/unsupported response proves nothing. Do not use Phone (3) images or assume another firmware revision shares the ABI.

Back up personal data and legally obtain verified original images for the exact firmware. Keep a complete coherent rollback set and offline access to a working USB/fastboot environment. The historical phone's other slot was not a usable recovery fallback; do not infer its current state. Temporary fastboot boot was not supported in historical tests. Recovery/fastbootd transitions had USB visibility failures in the virtualized host environment.

The final historical package changed five partitions together: boot, vendor_boot, vendor_dlkm, vbmeta_vendor and vbmeta. vendor_dlkm is logical and required fastbootd; other images used the appropriate bootloader mode. init_boot and dtbo were not changed by that final package. Do not turn this historical sequence into a universal command list, hard-code a slot, boot a partially written mixed set, or restore only stock boot with incompatible rebuilt drivers.

A future installation must first name the exact image hashes, partition and slot for every write, demonstrate compatible module/configuration and AVB relationships, provide the matching rollback plan and obtain explicit authorization. Packaging with a new key requires fresh review of the full chain. Keep dm-verity and metadata coherent; unlocking is not proof that mismatched descriptors are harmless. Never relock a bootloader with modified partitions.

After a separately authorized installation: establish Android boot completion, actual kernel config, module loading and errors, root/Manager operation, storage, radio/data/Wi-Fi/Bluetooth, display/touch/cameras/audio/sensors, thermals and suspend. In DroidSpaces, test mount visibility, propagation, networking, user-namespace creation and UID/GID mapping inside the actual container context, including the intended unprivileged case. Preserve SELinux/seccomp. Test SUSFS/NoMount rules individually and avoid hiding container root filesystems. Latest mapping/sandbox behavior remains unvalidated.

Returning to stock requires the complete compatible original set, correct live slot/modes and verified hashes, after its own explicit approval. The local archive contains historical stock candidates and rollback records, not a guarantee that they match a future updated phone. No current phone state, partition backup or recovery success was established by this archival task.
