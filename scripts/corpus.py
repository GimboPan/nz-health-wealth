"""Connect an optional user-owned Apple extractor to a private reference index.

No extractor or third-party transcript is redistributed with this project.
"""
import argparse,csv,hashlib,importlib.util,json,pathlib,re,shutil,sqlite3,sys

def build_index(records,folder):
    db=sqlite3.connect(folder/'search.sqlite')
    db.execute('DROP TABLE IF EXISTS transcript')
    db.execute('CREATE VIRTUAL TABLE transcript USING fts5(episode_id UNINDEXED,date UNINDEXED,timestamp UNINDEXED,speaker UNINDEXED,text,path UNINDEXED)')
    count=0
    for row in records:
        if row.get('status') not in ('reused','fetched') or not row.get('path'):continue
        text=pathlib.Path(row['path']).read_text()
        for match in re.finditer(r'\*\*(Speaker[^*]*?) · ([0-9:]+)\*\*\s*\n(.*?)(?=\n\*\*Speaker|\Z)',text,re.S):
            speaker,timestamp,body=match.groups()
            db.execute('INSERT INTO transcript VALUES (?,?,?,?,?,?)',(row['episode_id'],row['date'],timestamp,speaker,body.strip(),row['path']))
            count+=1
    db.commit();db.close()
    return count

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--show');ap.add_argument('--extractor',type=pathlib.Path)
    ap.add_argument('--existing-corpus',type=pathlib.Path)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    ap.add_argument('--inventory-only',action='store_true')
    ap.add_argument('--index-inventory',type=pathlib.Path,help='Index an existing local inventory JSON; no network')
    args=ap.parse_args();folder=args.output.resolve();folder.mkdir(parents=True,exist_ok=True)
    if args.index_inventory:
        records=json.loads(args.index_inventory.read_text())
        print(f'Indexed {build_index(records,folder):,} timestamped paragraphs.');return
    if not args.show or not args.extractor:ap.error('--show and --extractor are required for acquisition')
    spec=importlib.util.spec_from_file_location('user_apple_extractor',args.extractor.expanduser())
    at=importlib.util.module_from_spec(spec);sys.modules[spec.name]=at;spec.loader.exec_module(at)
    conn,tmp=at.open_library()
    try:episodes=[e for e in at.search(conn,'',show=args.show,limit=100000) if e.show.casefold()==args.show.casefold()]
    finally:conn.close();shutil.rmtree(tmp,ignore_errors=True)
    if not episodes:raise SystemExit('Show absent from local Podcasts library. Follow it and allow sync before retrying.')
    (folder/'transcripts').mkdir(exist_ok=True);records=[]
    for ep in episodes:
        rec=dict(episode_id=str(ep.track_id),date=ep.date,title=ep.title,apple_registered=bool(ep.transcript_id),duration_minutes=round((ep.duration or 0)/60,2),words=0,status='',path='',sha256='',source='')
        target=folder/'transcripts'/f'{ep.date}-{ep.track_id}.md'
        matches=[target] if target.exists() else []
        if not matches and args.existing_corpus:matches=sorted(args.existing_corpus.expanduser().glob(f'*-{ep.track_id}.md'))
        if matches:
            path=matches[0].resolve();content=path.read_text();body=content.split('\n---\n',1)[-1]
            words=len(re.sub(r'\*\*Speaker[^\n]+\*\*','',body).split());minutes=(ep.duration or 0)/60
            if minutes>=2 and words/minutes<at.MIN_WORDS_PER_MIN:rec.update(status='cached-stub',words=words)
            else:rec.update(status='reused',words=words,path=str(path),sha256=hashlib.sha256(content.encode()).hexdigest(),source='Existing Apple transcript; body density checked')
        elif not ep.transcript_id:rec['status']='no-apple-transcript'
        elif args.inventory_only:rec['status']='available-not-fetched'
        else:
            try:
                raw,source=at.fetch_ttml(ep.transcript_id);blocks,duration=at.parse_ttml(raw);blocks=at.merge_by_speaker(blocks)
                words=sum(len(b.text.split()) for b in blocks);minutes=(duration or ep.duration or 0)/60
                if not blocks or (minutes>=2 and words/minutes<at.MIN_WORDS_PER_MIN):rec.update(status='empty-or-stub',words=words)
                else:
                    content=at.render(ep,blocks,source,duration);target.write_text(content)
                    rec.update(status='fetched',words=words,path=str(target),sha256=hashlib.sha256(content.encode()).hexdigest(),source=source)
            except Exception as exc:rec.update(status='fetch-failed',source=str(exc).splitlines()[0])
        records.append(rec)
        if rec['status']!='reused':print(ep.date,ep.track_id,rec['status'],flush=True)
    (folder/'inventory.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    with (folder/'inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    count=build_index(records,folder)
    usable=[r for r in records if r['status'] in ('reused','fetched')]
    print(json.dumps(dict(episodes=len(records),usable=len(usable),words=sum(r['words'] for r in usable),paragraphs=count),ensure_ascii=False))

if __name__=='__main__':main()
