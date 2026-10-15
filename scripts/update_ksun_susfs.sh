#!/bin/bash
cd "$(dirname "$(realpath "$0")")"
cd ..

rm -rf ./components/KernelSU-Next
rm -rf ./components/susfs4ksu

git clone https://github.com/KernelSU-Next/KernelSU-Next.git "./components/KernelSU-Next"
git clone --branch gki-android13-5.15 --single-branch https://gitlab.com/simonpunk/susfs4ksu.git "./components/susfs4ksu"

