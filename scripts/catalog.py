"""Export a public episode inventory; never include transcript paths or text."""
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--health-inventory',type=pathlib.Path,required=True)
p.add_argument('--wealth-inventory',type=pathlib.Path,required=True)
a=p.parse_args();entries=json.loads((R/'content/entries.json').read_text());out=[]
for topic,show,showid,path in [('health','The Health Hub','1444362063',a.health_inventory),('wealth','Smart Money','1445636358',a.wealth_inventory)]:
 for row in json.loads(path.read_text()):
  refs=[e['id'] for e in entries if e.get('podcast') and e['podcast']['eid']==row['episode_id']]
  available=row['status'] in ('reused','fetched')
  out.append(dict(id=row['episode_id'],topic=topic,show=show,date=row['date'],title=row['title'],url=f'https://podcasts.apple.com/nz/podcast/id{showid}?i={row["episode_id"]}',transcriptAvailable=available,reviewStatus='selected-passages' if refs else 'indexed-unreviewed' if available else 'unavailable',entryIds=refs))
out.sort(key=lambda e:(e['date'],e['id']),reverse=True)
(R/'content/episodes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Public catalog: {len(out)} episodes; {sum(e["transcriptAvailable"] for e in out)} with transcripts; {sum(bool(e["entryIds"]) for e in out)} with selected citations.')
