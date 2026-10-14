# Privacy audit and exclusions

The export is assembled from pinned source snapshots and technical diffs, without any original .git directory, private author/committer identity, device reports or raw private logs. Public upstream copyright attribution is retained. The project history was inspected separately and a neutral, redacted technical patch log was retained only in the local archive.

Automated passes combine known private-pattern matching, PEM/private-key and service-token patterns, credential-assignment entropy checks, filename and symlink checks, and a source-only binary inventory. No gitleaks or detect-secrets executable was available; the bundled audit-release.py is an additional heuristic scanner, not a claim of equivalent comprehensive vendor coverage. Private search values and detection records with potentially identifying context stay outside both deliverables.

All 93 initially inventoried opaque binary assets in the public snapshots were excluded, rather than assuming that text scans inspect their content or licenses. An upstream SGX selftest private key was also removed. Upstream CI workflows are excluded. The corresponding source and notices remain; applications requiring those omitted assets are not advertised as buildable release packages.

For the local archive, compressed gzip/lz4/xz/bzip2 streams, ZIP/tar members and Android boot/vendor-boot payloads are decoded when recognized. EROFS images are extracted separately. Files with recognized private key material or device identifiers that cannot be safely redacted are excluded. Unneeded screenshots, opaque firmware archives and unsafe external links are excluded. Text logs and metadata are redacted; original hashes do not apply to altered metadata. Build intermediates and private signing directories are not archived.

The public final archive is extracted into a distinct directory and re-scanned. Every delivered regular file receives a content hash, with symlinks inventoried separately. Final audit outcomes are recorded in the delivery report and archive verification records.

Limits: heuristic detection cannot establish absence of every unknown identifier, secret, encoded payload or proprietary restriction. Public technical constants, crypto test vectors and upstream author information are not automatically personal device data. Rights for each integrated component, unfamiliar data formats and technical conclusions still merit human review. No publication is performed by this task. Future builds can embed the new builder's paths; re-audit any logs or binaries before sharing them.
