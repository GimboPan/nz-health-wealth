"""Validate citation boundaries and hashes against optional private inventories."""
import argparse,hashlib,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--inventory',type=pathlib.Path,action='append',required=True)
args=ap.parse_args();lookup={}
for p in args.inventory:
 for row in json.loads(p.read_text()):
  if row.get('path'):lookup[row['episode_id']]=row
def seconds(value):
 out=0
 for n in value.split(':'):out=out*60+int(n)
 return out
entries=json.loads((R/'content/entries.json').read_text());ledger=json.loads((R/'content/evidence-ledger.json').read_text());ledger={x['entryId']:x for x in ledger}
cache={};count=0;supplements=0
for e in entries:
 p=e.get('podcast')
 if not p:
  assert e.get('entryType')=='official-supplement' and e.get('sourceGap'),e['id'];supplements+=1;continue
 assert p['eid'] in lookup,(e['id'],'episode absent')
 if p['eid'] not in cache:
  text=pathlib.Path(lookup[p['eid']]['path']).read_text();ms=list(re.finditer(r'\*\*(Speaker[^*]*?) · ([0-9:]+)\*\*\s*\n',text));bs=[]
  for i,m in enumerate(ms):
   end=ms[i+1].start() if i+1<len(ms) else len(text)
   bs.append(dict(speaker=m[1],start=seconds(m[2]),end=seconds(ms[i+1][2]) if i+1<len(ms) else round(lookup[p['eid']]['duration_minutes']*60),text=text[m.end():end].strip()))
  cache[p['eid']]=bs
 bs=[b for b in cache[p['eid']] if b['speaker']==p['speaker'] and b['start']==p['startSeconds'] and b['end']==p['endSeconds']]
 assert len(bs)==1,(e['id'],'boundaries do not match')
 assert hashlib.sha256(bs[0]['text'].encode()).hexdigest()==p['segmentHash'],(e['id'],'hash mismatch')
 if p.get('identityEvidence'):
  identity=p['identityEvidence'];identity_blocks=[b for b in cache[p['eid']] if b['speaker']==identity['speaker'] and b['start']==identity['startSeconds'] and b['end']==identity['endSeconds']]
  assert len(identity_blocks)==1 and hashlib.sha256(identity_blocks[0]['text'].encode()).hexdigest()==identity['segmentHash'],(e['id'],'identity evidence mismatch')
 assert p['startSeconds']<p['endSeconds'] and p['contextChecked'] and not p['audioChecked'],e['id']
 assert ledger[e['id']]['segmentHash']==p['segmentHash'],(e['id'],'ledger mismatch')
 assert re.fullmatch(r'[0-9:]+–[0-9:]+',p['timestamp']),e['id']
 count+=1
print(f'PASS: {count} timestamped entries match original speaker blocks and SHA-256; {len(cache)} source episodes; {supplements} explicitly marked official supplements.')
