# Preparing a new local Git history

No remote repository was created and nothing was uploaded. The archive deliberately has no `.git` directory. Review LICENSES.md, STATUS.md and the privacy report first; no binary release is approved by these instructions.

From a freshly extracted, verified archive:

```sh
sha256sum -c CONTENTS.sha256
python3 scripts/audit-release.py .
git init
git add --force --pathspec-from-file=manifests/git-paths.txt
GIT_AUTHOR_NAME='Kernel Archive' GIT_AUTHOR_EMAIL='archive@example.invalid' \
GIT_COMMITTER_NAME='Kernel Archive' GIT_COMMITTER_EMAIL='archive@example.invalid' \
git -c user.name='Kernel Archive' -c user.email='archive@example.invalid' commit -m 'Import reviewed Pacman kernel source archive'
```

The explicit path list preserves source files which were tracked upstream despite upstream `.gitignore` rules (including `.scmversion` and several selftests). It excludes build outputs and dependencies. Do not replace it with an indiscriminate forced add after building. Review the staged file list before committing. The anonymous example identity is not an upstream author's identity. No push command is supplied.

Before any public distribution, resolve the integrated component license questions and repeat the audit on any newly added material. OEM images, vendor prebuilt objects, private keys, local archives and raw device reports must remain outside the public repository.
