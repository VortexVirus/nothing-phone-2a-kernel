# Kernel personnalisé Nothing Phone (2a) — Pacman

Export du développement réellement retrouvé pour **Nothing Phone (2a), Pacman, MT6886**, firmware Nothing OS **B4.0-251230-2052**. Ce projet ne concerne pas le Phone (3). Linux **5.15.178** : base Google GKI identifiée dans le firmware cible, sources vendor Nothing séparées.

Intégrations : KernelSU Next v3.4.0 avec port local SUSFS 2.3.0, configuration requise par DroidSpaces dont USER_NS, NoMount 2.0.0. Les optimisations FPSGO06 sont fournies en patch. L'expérience FPSGO07 est conservée séparément ; ce n'est pas la version installée historiquement.

Des compilations et un démarrage physique sont documentés. La création USER_NS a été observée ; le mapping UID/GID root et le sandbox DroidSpaces de la dernière variante ne sont pas validés. Une précédente configuration DroidSpaces était fonctionnelle selon le retour utilisateur. Aucun gain global de performances n'est démontré. Cet export est destiné à une revue technique et juridique, pas à un flash direct.

## Compilation rapide

Sur Debian x86_64, installer les dépendances de [BUILD](docs/BUILD.md), puis :

```sh
python3 scripts/setup-dependencies.py
python3 scripts/build.py --out "$PWD/.work/kernel-01" --dist "$PWD/.work/dist-01" --jobs 6
```

Utiliser une sortie neuve et des chemins sans espaces. Aucune opération téléphone n'est exécutée. Les nouvelles clés de signature doivent rester privées. Le kernel avec les options DroidSpaces ne doit pas être associé aux modules vendor stock.

`kernel/` contient les sources finales ; `components/` les composants épinglés ; `patches/`, `configs/`, `scripts/` et `manifests/` permettent d'en suivre et reproduire les changements. `release/` ne contient pas d'image OEM ni de binaire dont la publication n'a pas été revue.

Lire [STATUS](docs/STATUS.md), [INSTALLATION](docs/INSTALLATION.md), [LICENSES](LICENSES.md) et [CREDITS](CREDITS.md). Les attributions upstream sont conservées. La compatibilité des licences des composants intégrés doit être clarifiée avant diffusion des sources intégrées ou d'un binaire combiné. Historique Git privé et clés de signature sont exclus.

Une recompilation GKI isolée a réussi pendant l'archivage : 8 427 exports/CRC identiques et aucune différence ABI avec le kernel historique final. Ce nouveau binaire n'a pas été testé sur téléphone. Voir manifests/archive-build.json.
