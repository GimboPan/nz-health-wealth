"""Check a public release without requiring private podcast transcripts."""
import json,pathlib,re
R=pathlib.Path(__file__).resolve().parent.parent
read=lambda name:json.loads((R/'content'/name).read_text())
es=read('entries.json');eps=read('episodes.json');ledger=read('evidence-ledger.json');meta=read('meta.json')
ids={e['id'] for e in es};assert len(ids)==len(es),'duplicate entry IDs'
lookup={e['id']:e for e in eps};assert len(lookup)==len(eps),'duplicate episode IDs'
le={e['entryId']:e for e in ledger};assert len(le)==len(ledger),'duplicate evidence ledger IDs'
for e in es:
 assert e['sources'] and e['steps'] and e['english'],e['id']
 for s in e['sources']:assert s['url'].startswith('https://') and re.fullmatch(r'\d{4}-\d{2}-\d{2}',s['checked']),e['id']
 p=e.get('podcast')
 if p:
  assert p['eid'] in lookup and e['id'] in lookup[p['eid']]['entryIds'],e['id']
  assert lookup[p['eid']]['transcriptAvailable'] and lookup[p['eid']]['reviewStatus']=='selected-passages',e['id']
  assert p['startSeconds']<p['endSeconds'] and re.fullmatch('[a-f0-9]{64}',p['segmentHash']),e['id']
  assert p['show']==lookup[p['eid']]['show'] and p['date']==lookup[p['eid']]['date'],e['id']
  assert le[e['id']]['segmentHash']==p['segmentHash'] and le[e['id']]['speaker']==p['speaker'],e['id']
  assert p['contextChecked'] and not p['audioChecked'],e['id']
 else:assert e['entryType']=='official-supplement' and e['sourceGap'],e['id']
assert set(le)=={e['id'] for e in es if e.get('podcast')},'orphan ledger entries'
for ep in eps:
 assert set(ep['entryIds'])<=ids and ep['url'].startswith('https://podcasts.apple.com/'),ep['id']
 assert ep['reviewStatus']==('selected-passages' if ep['entryIds'] else 'indexed-unreviewed' if ep['transcriptAvailable'] else 'unavailable'),ep['id']
 for id in ep['entryIds']:assert next(e for e in es if e['id']==id)['podcast']['eid']==ep['id'],id
for c in meta['corpus']:
 rows=[e for e in eps if e['show']==c['name']]
 assert len(rows)==c['episodes'] and sum(e['transcriptAvailable'] for e in rows)==c['available'],c['name']
for folder in ['content','docs','src']:
 for f in (R/folder).rglob('*'):
  if f.is_file():
   s=f.read_text();assert not re.search(r'/Users/[^\s/]+/',s),f'private machine path: {f.name}'
   assert not re.search(r'(?m)^\*\*Speaker[^*]* · [0-9:]+\*\*',s),f'transcript body: {f.name}'
   assert not re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (RSA |OPENSSH )?PRIVATE KEY',s),f'credential pattern: {f.name}'
print(f'PASS public release: {len(es)} entries, {len(ledger)} citations, {len(eps)} episodes; references, statuses, coverage and private-data boundaries consistent.')
