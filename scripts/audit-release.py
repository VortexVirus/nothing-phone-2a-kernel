#!/usr/bin/env python3
"""Audit a source-only export; outputs locations/categories, never matched values.
Optional --private-patterns accepts a private JSON array and must stay outside release.
This is a heuristic check, not a guarantee that every unknown secret can be recognized.
"""
from pathlib import Path
import argparse,json,re,math,collections
p=argparse.ArgumentParser();p.add_argument('tree',type=Path);p.add_argument('--private-patterns',type=Path);a=p.parse_args();root=a.tree.resolve()
private=json.loads(a.private_patterns.read_text()) if a.private_patterns else []
patterns={
 'private-key':re.compile(rb'-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----[\r\n]+[A-Za-z0-9+/=\r\n]{32,}'),
 'service-token':re.compile(rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|AKIA[A-Z0-9]{16})\b'),
 'keybox-data':re.compile(rb'<Keybox\b[^>]*DeviceID='),
}
assignment=re.compile(rb'''(?im)(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd|secret[_-]?key)\s*[=:]\s*["']([A-Za-z0-9_+/=.-]{16,})["']''')
findings=[];count=0
for f in sorted(root.rglob('*')):
 rel=str(f.relative_to(root))
 if f.is_symlink():
  if not f.exists() or not f.resolve().is_relative_to(root):findings.append({'path':rel,'category':'external-or-broken-symlink'})
  continue
 if not f.is_file():continue
 count+=1;b=f.read_bytes();categories=[]
 if '.git' in f.relative_to(root).parts:categories.append('private-history-not-allowed')
 if b'\0' in b[:8192]:categories.append('opaque-binary-or-archive-review-required')
 if any(v.encode() in b for v in private):categories.append('known-private-pattern')
 for name,rx in patterns.items():
  if rx.search(b):categories.append(name)
 lower=b.lower()
 if any(v in lower for v in [b'password',b'passwd',b'api_key',b'api-key',b'access_token',b'auth_token',b'client_secret',b'secret_key']):
  for m in assignment.finditer(b):
   v=m[1];c=collections.Counter(v);h=-sum(n/len(v)*math.log2(n/len(v)) for n in c.values())
   if h>=3.5:categories.append('credential-assignment-needs-review')
 for category in sorted(set(categories)):findings.append({'path':rel,'category':category})
print(json.dumps({'files':count,'findings':findings,'automated_pass':not findings},indent=2))
raise SystemExit(bool(findings))
