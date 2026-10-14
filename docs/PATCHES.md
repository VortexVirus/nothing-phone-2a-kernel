# Patches and recovered modifications

The custom GKI is based on Google GKI, not a direct checkout of the vendor OEM kernel. The OEM vendor delta is listed separately. No unrelated hardware patch or optimization is inferred from a branch name.

`gki-custom.patch` is the exact original Git diff from 18a89f1307e251f1533266476c36a9bae2a0c033 to 90700ba133db2fb1d2b05519d45de38ad3d148e1 (before archive-only link adjustment). `ksu-susfs-port.patch` is the local Next delta from official v3.4.0 to e7f85f7c439f157ec25a3c682e92886bb5f1546a. `fpsgo06.patch` is the exact OEM delta through the installed performance revision; FPSGO07 is separately named experimental. `vendor-modules.patch` is empty: the module repository was unchanged, while configuration and build layout changed.

KernelSU: built-in drivers wiring; imported pershoot kernel delta only, with stable-register/Kbuild conflict resolutions. The local sys_read bridge uses the single-argument signature required by this 5.15 SUSFS call site.

SUSFS: VFS lookup/stat/open/read/exec/readdir/mount inspection, proc maps/fd/bootconfig, kallsyms, uname/reboot and SELinux integration. The task_mmu show_smap adaptation applies filtering to the actual data VMA obtained via get_data_vma, preserving the stock path for unaffected mappings. See enabled feature matrix in STATUS.md; configuration is not runtime proof.

DroidSpaces: configuration fragment rather than a new in-kernel container engine. USER_NS was added later. Six UID/GID exports already defined by the kernel were added to the Nothing KMI allowlist because trimming removed vendor-required functions. No CRC/CFI bypass was applied.

NoMount: four upstream kernel files copied, Kconfig depends on KEYS added, fs/Kconfig and fs/Makefile wiring, NOMOUNT=y. No new public kernel structure modification by this integration.

FPSGO06: only fbt_cpu.c changed relative to OEM. Copy dependencies only for the selected maximum, skip scalar-only copies, remove an intermediate dependency buffer under the existing mutex, replace per-cluster boost arrays with scalars. FullLTO eliminated one intermediate source change already; no binary gain was claimed for that step. Two allocation/free pairs are removed in fbt_do_boost; historical ARM64 function size 1088→980 bytes. Thresholds, governors, headers and locks were not changed. FPSGO07 groups per-call loading snapshots and is not in the installed baseline.

Archive-only changes: relative KernelSU link points inside the export; export-ksu-version.patch fixes version/tag without private history; kernel/.scmversion pins an export suffix; private selftest key and opaque assets excluded. Build wrapper creates fresh signing material and omits generic boot packaging. These changes are distinct from recovered kernel features.

## gki-custom — changed files

```text
 android/abi_gki_aarch64_nothing                |    8 +
 arch/arm64/configs/pacman_droidspaces.fragment |   16 +
 drivers/Kconfig                                |    1 +
 drivers/Makefile                               |    2 +
 drivers/input/input.c                          |   11 +
 drivers/kernelsu                               |    1 +
 fs/Kconfig                                     |    1 +
 fs/Makefile                                    |    4 +
 fs/exec.c                                      |   37 +
 fs/namei.c                                     |  237 ++++
 fs/namespace.c                                 |  255 ++++
 fs/nomount/Kconfig                             |    9 +
 fs/nomount/Makefile                            |    5 +
 fs/nomount/nomount.c                           | 1521 +++++++++++++++++++++++
 fs/nomount/nomount.h                           |  329 +++++
 fs/notify/fdinfo.c                             |   78 ++
 fs/open.c                                      |   28 +
 fs/proc/base.c                                 |   23 +
 fs/proc/bootconfig.c                           |   13 +
 fs/proc/fd.c                                   |   70 ++
 fs/proc/task_mmu.c                             |   68 ++
 fs/proc_namespace.c                            |  178 +++
 fs/read_write.c                                |   10 +
 fs/readdir.c                                   |  109 ++
 fs/stat.c                                      |   90 ++
 fs/statfs.c                                    |   81 ++
 fs/super.c                                     |   24 +
 fs/susfs.c                                     | 1538 ++++++++++++++++++++++++
 include/linux/susfs.h                          |  243 ++++
 include/linux/susfs_def.h                      |  162 +++
 kernel/kallsyms.c                              |   31 +
 kernel/reboot.c                                |   12 +
 kernel/sys.c                                   |   15 +
 mm/memory.c                                    |   12 +
 security/selinux/avc.c                         |   21 +-
 security/selinux/hooks.c                       |   45 +
 security/selinux/selinuxfs.c                   |  143 +++
 37 files changed, 5430 insertions(+), 1 deletion(-)
```

## ksu-susfs-port — changed files

```text
 kernel/Kbuild                      |  44 ++++-
 kernel/Kconfig                     |  96 ++++++++++-
 kernel/core/init.c                 |  51 ++++++
 kernel/extras.c                    |  22 ++-
 kernel/feature/adb_root.c          | 163 +++++++++++++++++--
 kernel/feature/adb_root.h          |   4 +
 kernel/feature/kernel_umount.c     |   9 +-
 kernel/feature/selinux_hide.c      | 169 +++++++++++---------
 kernel/feature/selinux_hide.h      |  15 ++
 kernel/feature/sucompat.c          | 320 ++++++++++++++++++++++++++++++++++++-
 kernel/feature/sucompat.h          |  16 +-
 kernel/hook/setuid_hook.c          | 169 ++++++++++++++++++--
 kernel/hook/setuid_hook.h          |   4 +
 kernel/hook/syscall_event_bridge.c |  20 ++-
 kernel/policy/allowlist.c          |   2 +
 kernel/policy/app_profile.c        |  27 +++-
 kernel/policy/app_profile.h        |   2 +-
 kernel/runtime/boot_event.c        |  21 ++-
 kernel/runtime/ksud.h              |  20 +++
 kernel/runtime/ksud_integration.c  | 197 ++++++++++++++++++-----
 kernel/selinux/rules.c             |  11 ++
 kernel/selinux/selinux.c           | 105 +++++++++++-
 kernel/selinux/selinux.h           |  11 ++
 kernel/sulog/event.c               |  84 ++++++++++
 kernel/sulog/event.h               |   4 +
 kernel/supercall/dispatch.c        | 142 ++++++++++++++++
 kernel/supercall/internal.h        |   2 +
 kernel/supercall/supercall.c       | 195 +++++++++++++---------
 kernel/supercall/supercall.h       |   4 +
 29 files changed, 1681 insertions(+), 248 deletions(-)
```

## fpsgo06 — changed files

```text
 .../performance/fpsgo_v3/fbt/src/fbt_cpu.c         | 64 ++++++++--------------
 1 file changed, 23 insertions(+), 41 deletions(-)
```

## fpsgo07-experimental — changed files

```text
 .../performance/fpsgo_v3/fbt/src/fbt_cpu.c         | 44 +++++++++++++++-------
 1 file changed, 30 insertions(+), 14 deletions(-)
```

## vendor-modules — changed files

```text
```
