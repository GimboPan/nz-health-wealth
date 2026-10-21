"""Build one self-contained HTML page using Python's standard library."""
import json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parent.parent
entries=json.loads((ROOT/'content/entries.json').read_text())
meta=json.loads((ROOT/'content/meta.json').read_text())
assert len({x['id'] for x in entries})==len(entries),'Duplicate entry ID'
required=['id','topic','category','title','summary','steps','cost','limit','english','sources','official','status']
for e in entries:
    assert all(k in e for k in required),f'Missing fields: {e.get("id")}'
    assert re.fullmatch(r'[a-z0-9-]+',e['id'])
    assert e['topic'] in ('health','wealth')
    assert e['steps'] and all(isinstance(s,str) for s in e['steps'])
    assert all(s['url'].startswith('https://') for s in e['sources'])
    if e['status']=='本次核对':assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',e['checked'])
    if e.get('podcast'):
        assert e['podcast']['url'].startswith('https://podcasts.apple.com/')
        assert str(e['podcast']['eid']) in e['podcast']['url']
        assert re.fullmatch(r'[0-9:]+–[0-9:]+',e['podcast']['timestamp'])
        assert e['podcast']['contextChecked'] and e['podcast']['startSeconds']<e['podcast']['endSeconds']
    else:
        assert e.get('entryType')=='official-supplement' and e.get('sourceGap')
text=(ROOT/'src/page.template.html').read_text()
research=json.loads((ROOT/'content/research-map.json').read_text())
episodes=json.loads((ROOT/'content/episodes.json').read_text())
data=json.dumps(dict(entries=entries,meta=meta,research=research,episodes=episodes),ensure_ascii=False).replace('<','\\u003c')
text=text.replace('/* STYLES */',(ROOT/'src/styles.css').read_text()).replace('/* DATA */','window.GUIDE_DATA='+data+';').replace('/* APP */',(ROOT/'src/app.js').read_text())
counts={t:sum(e['topic']==t for e in entries) for t in ('health','wealth')}
citations=[e['podcast'] for e in entries if e['podcast']]
values=dict(version=meta['version'],observedDate=meta['observedDate'],corpusObservedDate=meta.get('corpusObservedDate',meta['observedDate']),entryCount=len(entries),healthCount=counts['health'],wealthCount=counts['wealth'],
 timestampedCount=len(citations),supplementCount=len(entries)-len(citations),corpusCount=sum(c['available'] for c in meta['corpus']),
 distinctBodies=sum(x['distinctBodies'] for x in research['topics'].values()),sourceEpisodes=len({x['eid'] for x in citations}),uniquePassages=len({x['evidenceId'] for x in citations}),episodeCount=len(episodes))
for key,value in values.items():text=text.replace('{{'+key+'}}',str(value))
assert not re.search(r'\{\{[a-zA-Z]+\}\}',text),'Unfilled template value'
assert '/* DATA */' not in text and '/* APP */' not in text
assert '/Users/' not in text,'Private machine path leaked into public HTML'
(ROOT/'dist').mkdir(exist_ok=True)
(ROOT/'dist/index.html').write_text(text)
print(f'Built dist/index.html: {len(entries)} entries, {len(text.encode()):,} bytes')
