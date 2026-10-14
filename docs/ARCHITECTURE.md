# Architecture and recovered source layout

The target firmware uses Google GKI `18a89f1307e251f1533266476c36a9bae2a0c033` (android13-5.15-2025-03_r4, build 13471816). Local historical evidence records a byte-identical Google Image.lz4 and OEM kernel payload. The Nothing kernel publication `02f45fecd3aa6780740aca0a79a120b810f7c744` is used separately for vendor drivers. These trees are not interchangeable.

`kernel/` exports the final custom GKI commit `90700ba133db2fb1d2b05519d45de38ad3d148e1`. `drivers/kernelsu` links relatively to `components/KernelSU-Next/kernel`, wired by drivers/Kconfig and drivers/Makefile. Next is built-in, not an init_boot LKM. The SUSFS patch changes VFS, procfs, memory inspection and SELinux paths; Next's local port implements the corresponding bridge and commands. `fs/nomount` contains the built-in path redirection subsystem and requires KEYS.

DroidSpaces is a userspace container system. Its pinned repository is a reference and source snapshot, not an in-kernel daemon. Integration here consists of kernel configuration and matching vendor rebuilds. SYSVIPC, POSIX_MQUEUE, PID_NS, IPC_NS, USER_NS, CGROUP_DEVICE, CGROUP_PIDS, DEVTMPFS, bridge netfilter, nftables and address-type matching complement the GKI baseline. Mount namespaces and cgroup v2 are not independent missing CONFIG symbols. NF_CT_NETLINK is the real symbol on this tree; the historical fragment contains a redundant unsupported alias.

Changing IPC/cgroup options alters task_struct, net, cgroup, css_set and cgroup_root layouts. The combined kernel cannot safely load the original modules merely by keeping the release string. CFI, Full LTO, MODVERSIONS, symbol trimming and signature protection remain enabled. Six UID/GID conversion exports were explicitly retained for USER_NS vendor users.

The final historical device package combines USER_NS GKI, 410 selected vendor modules at 435 paths, and FPSGO06. It contains boot, vendor_boot, vendor_dlkm, vbmeta_vendor and vbmeta; init_boot is not part of this package. OEM ramdisk/DTB/bootconfig and AVB metadata are required for device packaging. Those files are only in the private local archive.

The local complete archive additionally contains OEM source snapshots, historical recipes/logs/artefacts, toolchain material and new build outputs, subject to the documented exclusions. Public source snapshots do not preserve private Git metadata. Branches and commits are listed in manifests/repository-inventory.json; source changes are recoverable from snapshots and patches.
