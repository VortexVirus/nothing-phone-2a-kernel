# Reconstructed development chronology

Compiled from local Git subjects and dated technical records; this is not imported private Git history. Earlier documents contain superseded intermediate states. STATUS.md resolves the final state.

- 2026-10-02: identify firmware, exact OEM source pins and byte-identical Google GKI; restore historical clang/pipeline; build stock and repeat for reproducibility; prepare initial Next integration.
- 2026-10-03: compile Next and SUSFS port; measure DroidSpaces ABI break; rebuild and audit vendor modules; correct TOP/user-mode/supplement recipes; preserve TUI closure exception; create coherent OEM-based packages and record physical use. Integrate and build NoMount; start FPSGO optimization tests.
- 2026-10-04: archive build caches and preserve storage checks, without inferring new runtime validation.
- 2026-10-05: FPSGO06 scalar optimization and host tests; USER_NS first build, failed vendor exports, six-export KMI correction, final vendor rebuild; recompile FPSGO06 for USER_NS; package and historical physical boot; measure before/after with no overall gain; sandbox mapping remains open. FPSGO07 and MGLRU/RAM research remain separate.
- 2026-10-13: independent export, artifact rehashing, privacy exclusions, fresh isolated build attempt, documentation and archive verification. Consult archive-build.json and final audit report for actual outcomes.

## Exact local technical commits

### gki-custom

```text
90700ba133db2fb1d2b05519d45de38ad3d148e1 kmi: retain namespace UID/GID exports required by Pacman vendor modules
b1379f8fe0410ef53f96f1be3f294f3c17560957 arm64: enable user namespaces for Pacman DroidSpaces sandboxing
515e10a550524692829dfad3ee2c7691ff74b468 Integrate maxsteeel NoMount v2.0.0 built-in on combined DroidSpaces kernel
9439133e7f0343e5dd6f52bd6d4e03c418d9b7fd Add minimal DroidSpaces configuration fragment for ABI evaluation
8639d0d67195a4761b5ebcf7436ccc53d0664980 Integrate SUSFS v2.3.0 Android13 5.15 patch with stable Next port
e9af941faf2cb76f1a96a4bb0ea69e7ae3959976 Integrate pinned KernelSU Next v3.4.0 built-in driver
```

### ksu-susfs-port

```text
e7f85f7c439f157ec25a3c682e92886bb5f1546a Match SUSFS 5.15 read hook prototype without unused arguments
a0e34623d408aadf12784c297f5858a8a7f5a4ae Port pershoot SUSFS 2.3 integration 1b9194d8 to Next v3.4.0 for compatibility testing
```

### fpsgo06

```text
313c21a9dc2358667e9640e35738d2e9cab49a5e fpsgo: replace per-cluster temporary boost arrays with scalars
a76624c067205bb593641f90dd65fa2824e1966c fpsgo: eliminate temporary dependency buffer under fbt mutex
37964b3716063357437aea2a00f61e364c8ff1b9 fpsgo: skip dependency copies for scalar-only maximum queries
e6eebb4ac1bc5489bb9c066a9c7543d775cb13e0 fpsgo: copy dependencies only for the selected maximum boost
```

### fpsgo07-experimental

```text
800e6f1cf0c85c41bb60baa56a3cb17d4898214d fpsgo: group per-call loading snapshots without increasing payload size
```
