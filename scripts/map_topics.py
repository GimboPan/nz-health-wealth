"""Map local transcripts to candidate themes. Lexical hits are not conclusions."""
import argparse,collections,hashlib,json,pathlib,re
R=pathlib.Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--health-inventory',type=pathlib.Path,required=True)
ap.add_argument('--wealth-inventory',type=pathlib.Path,required=True)
ap.add_argument('--output',type=pathlib.Path,required=True)
args=ap.parse_args()
taxonomy=json.loads((R/'content/topic-taxonomy.json').read_text())
report={'method':'按正文关键词匹配，剔除含明确广告提示的段落，再按正文精确去重；仅供候选发现，不表示语义审核或全部蒸馏。','topics':{}}
ad=re.compile(r'Harbou?r Income Fund|Morningstar.{0,50}Fund Manager|Consumer.s Guide to Hearing Aids|not intended as personali[sz]ed advice',re.I)
for topic,inventory in [('health',args.health_inventory),('wealth',args.wealth_inventory)]:
 rows=json.loads(inventory.read_text());bodies=collections.defaultdict(list);counts=collections.Counter();excluded=0;block_count=0
 for row in rows:
  if not row.get('path'):continue
  text=pathlib.Path(row['path']).read_text().split('\n---\n',1)[-1]
  blocks=[b.strip() for b in re.split(r'\*\*Speaker[^\n]+\*\*',text) if b.strip()]
  normalized=' '.join(' '.join(blocks).split());h=hashlib.sha256(normalized.encode()).hexdigest()
  bodies[h].append(row['episode_id'])
  if len(bodies[h])>1:continue
  keep=[]
  for block in blocks:
   block_count+=1
   if ad.search(block):excluded+=1
   else:keep.append(block.lower())
  body='\n'.join(keep)
  for name,terms in taxonomy[topic].items():
   if any(term.lower() in body for term in terms):counts[name]+=1
 report['topics'][topic]=dict(availableFiles=sum(bool(x.get('path')) for x in rows),distinctBodies=len(bodies),
  exactDuplicateGroups=[v for v in bodies.values() if len(v)>1],scannedBlocks=block_count,
  adPatternExcludedBlocks=excluded,candidateEpisodeCounts=dict(counts))
args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:{x:v[x] for x in ('availableFiles','distinctBodies','scannedBlocks','adPatternExcludedBlocks')} for k,v in report['topics'].items()},ensure_ascii=False))
