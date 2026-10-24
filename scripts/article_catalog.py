"""Generate the public article inventory and synchronize known website artifacts."""
import argparse,json,pathlib,re,sys

ROOT=pathlib.Path(__file__).resolve().parent.parent

def catalog():
    data=json.loads((ROOT/'content/articles.json').read_text())
    ids=set();urls=set()
    for a in data['articles']:
        assert re.fullmatch('[a-z0-9-]+',a['id']) and a['id'] not in ids
        assert a['url'] not in urls and a['url'].startswith('https://gimbo.co.nz/ideas/')
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',a['updated'])
        assert a['repositoryPath'].startswith('docs/guides/') and '..' not in a['repositoryPath']
        assert (ROOT/a['repositoryPath']).read_text().startswith('# '+a['title']+'\n')
        assert a['kind'] in ('article','collection') and a['topic'] in ('health','wealth')
        ids.add(a['id']);urls.add(a['url'])
        for old in a.get('related',[]):
            assert old['url'].startswith('https://gimbo.co.nz/fitness/')
    return data

def inventory(data):
    lines=['# 专题文章目录','',f'[Ideas统一入口]({data["entryUrl"]}) · [交互指南]({data["guide"]["url"]})','','本目录由`content/articles.json`生成；网站目录使用同一份清单。','','| 专题文章 | 网站阅读 | GitHub原文 | 日期性质 |','| --- | --- | --- | --- |']
    for a in data['articles']:
        path=pathlib.PurePosixPath(a['repositoryPath']).relative_to('docs')
        lines.append(f'| {a["title"]} | [阅读全文]({a["url"]}) | [原文]({path}) | {a["dateLabel"]} {a["updated"]} |')
    for a in data['articles']:
        if a.get('related'):
            lines+=['',f'## {a["title"]}中的Fitness原文','','以下文章及原网址保留，未冒充本次重新核验。']
            for old in a['related']:
                lines+=['',f'- [{old["title"]}]({old["url"]})：{old["summary"]} {old["note"]}。']
    lines+=['','新增或调整专题时同步修改清单和原文，再按[发布流程](PUBLISHING.md)生成及核对两端内容。']
    return '\n'.join(lines)+'\n'

def website_files(data):
    es=json.loads((ROOT/'content/entries.json').read_text());meta=json.loads((ROOT/'content/meta.json').read_text())
    release=dict(version=meta['version'],date=meta['observedDate'],repository=meta['repository'],entries=len(es),healthEntries=sum(e['topic']=='health' for e in es),wealthEntries=sum(e['topic']=='wealth' for e in es),timestamped=sum(bool(e.get('podcast')) for e in es),citedEpisodes=len({e['podcast']['eid'] for e in es if e.get('podcast')}),catalogEpisodes=len(json.loads((ROOT/'content/episodes.json').read_text())),officialSupplements=sum(not e.get('podcast') for e in es))
    files={
        'src/data/nz-health-wealth-directory.json':json.dumps(data,ensure_ascii=False,indent=2)+'\n',
        'src/data/nz-health-wealth-release.json':json.dumps(release,ensure_ascii=False,indent=2)+'\n',
        'public/ideas/nz-health-wealth-guide.html':(ROOT/'dist/index.html').read_text()
    }
    for a in data['articles']:
        slug=a['url'].removeprefix('https://gimbo.co.nz/ideas/').rstrip('/')
        assert re.fullmatch('[a-z0-9-]+',slug)
        source=(ROOT/a['repositoryPath']).read_text().split('\n\n',2)
        assert len(source)==3,'Article needs title, metadata and body blocks'
        front=dict(layout='../../layouts/HealthWealthArticle.astro',title=a['title'],description=a['summary'],checked=a['updated'],checkedLabel=a['dateLabel'],metaNote=a['metaNote'],guideHref=a['guideHref'],guideLabel=a['guideLabel'],source=meta['repository']+'/blob/main/'+a['repositoryPath'])
        header='---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in front.items())+'\n---\n\n'
        files['src/pages/ideas/'+slug+'.md']=header+source[2]
    return files

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--website',type=pathlib.Path);ap.add_argument('--check',action='store_true');args=ap.parse_args()
    data=catalog();files={ROOT/'docs/ARTICLES.md':inventory(data)}
    if args.website:
        assert (args.website/'src/layouts/HealthWealthArticle.astro').is_file(),'Expected existing website layout'
        files.update({args.website/name:text for name,text in website_files(data).items()})
    different=[str(p) for p,text in files.items() if not p.exists() or p.read_text()!=text]
    if args.check:
        if different:print('Out of sync:\n'+'\n'.join(different));sys.exit(1)
    else:
        for p,text in files.items():p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    print(('Checked' if args.check else 'Generated')+f' article catalog: {len(data["articles"])} thematic articles, '+str(sum(len(a.get('related',[])) for a in data['articles']))+' preserved Fitness references.')

if __name__=='__main__':main()
