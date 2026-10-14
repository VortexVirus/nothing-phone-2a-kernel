# Factual status at archival

Historical evidence ends on 2026-10-05. Archive inspection was performed on 2026-10-13. No phone was accessed, flashed or rebooted during archival. See archive-build.json for the independently attempted new compilation; historical success does not imply success of that run.

| Component | In source / configuration | Historically compiled | Host evidence | Phone evidence | Remaining limits |
|---|---|---|---|---|---|
| KernelSU Next | v3.4.0 `1a879d6a866f80b1fa1c1009a2ffa747873cbb5e`, local SUSFS port `e7f85f7c439f157ec25a3c682e92886bb5f1546a`; KSU=y | Yes, final userns-02 code 0 | Hashes, symbols, ABI checks | Historical Next+SUSFS device use and latest combined boot documented | Root unavailable to final ADB session; no new manager/root validation |
| SUSFS | 2.3.0 `687d2d18d94cb2e3e72d1074778d58384d58e379` | Yes | Config, object integration, source port, final kernel | Combined kernel boots; earlier user feedback | Each hiding/spoofing/redirection API not exhaustively tested |
| DroidSpaces | requirements from `14a8dba3bedfd42cfc9b6f10ce06b72e688c7523`; container features enabled | Kernel prerequisites yes; application not rebuilt by this archive | Vendor ABI changes measured, modules rebuilt | Earlier containers functional according to user; latest USER_NS inode creation observed | Toybox mapping test returned overflowuid 65534 with empty maps; sandbox not validated |
| NoMount | 2.0.0 `b8d268353b4e7ecc53c67d1816a626b7d6579201`; NOMOUNT=y | Yes | Initialization symbols and ABI/CRC | Boot and general functioning reported | Matching userspace protocol/rules and namespace interactions not fully validated |
| FPSGO06 | `313c21a9dc2358667e9640e35738d2e9cab49a5e` | Yes, including USER_NS rebuild | C harnesses, ASan/UBSan, contracts, DWARF, disassembly | Coherent package flashed historically and Android booted | Installed .ko could not be read back by ADB; no global performance gain |
| FPSGO07 | `800e6f1cf0c85c41bb60baa56a3cb17d4898214d` | Separate experimental records only | See historical records | Not the installed reference | Never silently substitute for FPSGO06 |
| MGLRU | CONFIG_LRU_GEN=y, default enabled option off | In kernel | Config inspection | Runtime state unknown | No RAM tuning or benefit demonstrated |

SUSFS options actually enabled: SUS_PATH, SUS_MOUNT, SUS_KSTAT, SPOOF_UNAME, ENABLE_LOG, HIDE_KSU_SUSFS_SYMBOLS, SPOOF_CMDLINE_OR_BOOTCONFIG, OPEN_REDIRECT and SUS_MAP. Enabled does not mean individually exercised. Global non-su mount hiding defaults false in fs/susfs.c; userspace can change it. DroidSpaces upstream explicitly does not support SUSFS. The policy must be checked in actual namespaces; root UID alone is insufficient to infer SELinux policy.

## Known failures and boundaries

DroidSpaces configuration first produced 5753 changed CRCs and affected all 435 original vendor module paths. Rebuilt drivers are required. USER_NS initially caused modpost UID/GID failures; retaining six existing exports fixed the rebuild. Final GKI exports: 8421 unchanged CRCs plus six additions. ABI diff returned 8 for additive functions, not 0 for strict identity.

The final vendor selection contains 410 unique modules / 435 locations. Absolute closure remains false because optional t_base_tui imports gt9895 symbols absent in the original stock manifest. No new protected-symbol, CRC, CFI or vermagic error was recorded. Six representative type layouts were inspected; that is not exhaustive validation of proprietary objects or all private interfaces.

Historical new kernel config SHA256: `f77db4bbe60be643fd983fd8c08c51b207364233eefe31612f79bb84fa6a4774`. Historical Image SHA256: `5acf0485be05e034e40a27d4fbd7974ce6378dc6c61902a7f9d43c578c4844d3`. Archive verification rehashed the available recorded artefacts; see manifests/historical-artifact-verification.json. Sanitized metadata have separate archive hashes.

## Measured performance

Before/after native runs lasted about 600 seconds each, with 2180 analyzed passes per run and correct calculation checksums. CPU median 108.481 → 108.559 ms (+0.073%); memory-read median 42.745 → 42.706 ms (-0.090%). Settings launch 431 → 462 ms (+7.19%), repeated after-run 477 ms (+10.67%). One janky frame in each scrolling sequence. No overall gain demonstrated; launch slowdown is an observation, not proven kernel causality. SoC temperatures, charge state and background activity were not identical. No game/GPU/battery/multicore validation follows from these tests.

## Archival rebuild outcome

The independent source-export build completed successfully on 2026-10-13 (exit 0). Image, Image.gz, Image.lz4, vmlinux, symbol metadata and two generic GKI modules were produced. Both compressed images decode exactly to Image. All 8427 exports and CRCs match historical userns-02; actual DWARF dump and ABI comparison returned 0. No compiler warning/error or clock-skew line was found. This validates the host build and inspected interfaces, not a phone installation. The new release string is 5.15.178-g90700ba133db2; signatures and binaries differ from the historical package. No new vendor/package or physical validation was performed. New Image SHA256: af40992e6af896ddde640bfa54393a0eadfea17ab359a87864e60e699d803fc7.
