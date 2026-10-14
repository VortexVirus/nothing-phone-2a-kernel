#!/usr/bin/env python3
"""Retrieve pinned public build tools. Downloads only; does not access a device."""
from pathlib import Path
import argparse, subprocess, json, hashlib, urllib.request, tarfile, os, xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--pipeline',type=Path,default=root/'.deps/gki');args=a.parse_args();pipeline=args.pipeline.resolve();pipeline.mkdir(parents=True,exist_ok=True)
lock=json.loads((root/'manifests/dependencies.json').read_text())
for entry in lock['pipeline_projects']:
 dest=pipeline/entry['path'];rev=entry['revision']
 if dest.exists() and any(dest.iterdir()):
  actual=subprocess.check_output(['git','-C',str(dest),'rev-parse','HEAD'],text=True).strip()
  if actual!=rev:raise SystemExit('Existing dependency differs: '+entry['path'])
 else:
  dest.mkdir(parents=True,exist_ok=True)
  subprocess.run(['git','init',str(dest)],check=True)
  subprocess.run(['git','-C',str(dest),'fetch','--depth=1','https://android.googlesource.com/'+entry['name'],rev],check=True)
  subprocess.run(['git','-C',str(dest),'checkout','--detach','FETCH_HEAD'],check=True)
for entry in lock['toolchain_archives']:
 cache=pipeline/'.downloads'/entry['archive'];cache.parent.mkdir(exist_ok=True)
 if not cache.exists():
  url='https://android.googlesource.com/'+entry['repository']+'/+archive/'+entry['commit']+'/'+entry['subdir']+'.tar.gz'
  temp=cache.with_suffix('.partial')
  with urllib.request.urlopen(url,timeout=600) as src,temp.open('wb') as dst:
   while chunk:=src.read(8*1024*1024):dst.write(chunk)
  temp.rename(cache)
 with cache.open('rb') as f:actual=hashlib.file_digest(f,'sha256').hexdigest()
 if actual!=entry['sha256']:raise SystemExit('Dependency archive checksum mismatch')
 relative='prebuilts/clang/host/linux-x86/clang-r450784e' if entry['subdir'].startswith('clang-') else 'prebuilts/ndk-r23/toolchains/llvm/prebuilt/linux-x86_64/sysroot'
 dest=pipeline/relative
 if not dest.exists():
  dest.mkdir(parents=True)
  with tarfile.open(cache) as archive:archive.extractall(dest,filter='data')
for project in ET.parse(root/'manifests/android-13471816.xml').findall('project'):
 if (pipeline/project.attrib['path']).exists():
  for link in project.findall('linkfile'):
   dest=pipeline/link.attrib['dest'];dest.parent.mkdir(parents=True,exist_ok=True)
   if not dest.exists() and not dest.is_symlink():dest.symlink_to(os.path.relpath(pipeline/project.attrib['path']/link.attrib['src'],dest.parent))
for name in ['common-nomount-userns','.source_date_epoch_dir']:
 dest=pipeline/name
 if not dest.exists():dest.symlink_to(os.path.relpath(root/'kernel',pipeline))
print('Pinned pipeline ready. No build or device operation performed.')
