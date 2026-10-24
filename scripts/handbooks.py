"""Generate GitHub-readable field guides from the same structured content as the UI."""
import collections,json,pathlib
from article_catalog import catalog,inventory
R=pathlib.Path(__file__).resolve().parent.parent
es=json.loads((R/'content/entries.json').read_text());meta=json.loads((R/'content/meta.json').read_text());episodes=json.loads((R/'content/episodes.json').read_text())
for topic,title in [('health','Health · 新西兰求医与健康支持'),('wealth','Wealth · 新西兰金钱与生活安排')]:
 items=[e for e in es if e['topic']==topic]
 lines=[f'# {title}\n',f'v{meta["version"]} · 内容更新截至 {meta["observedDate"]} · {len(items)} 条。\n','[回到项目首页](../README.md) · [来源与核对记录](DISTILLATION.md)\n','这些是面向实际场景的编辑整理。节目经历、现行资料和编辑步骤分别标注；未听音或经医疗、法律、财务专业人员逐条审阅。\n','## 目录\n']
 for cat in dict.fromkeys(e['category'] for e in items):
  lines.append(f'### {cat}\n')
  lines += [f'- [{e["title"]}](#{e["id"]})' for e in items if e['category']==cat]
 for e in items:
  lines += [f'\n<a id="{e["id"]}"></a>\n',f'## {e["title"]}\n',e['summary']+'\n','### 下一步\n']
  lines += [f'{i+1}. {s}' for i,s in enumerate(e['steps'])]
  lines += [f'\n**费用与成本：** {e["cost"]}\n',f'**适用边界：** {e["limit"]}\n',f'**可以这样问（编辑撰写）：** {e["english"]}\n',f'**公共资料：** {e["official"]}\n']
  lines += [f'- [{s["label"]}]({s["url"]}) · 核对 {s.get("checked") or "待核实"}' for s in e['sources']]
  if e.get('correction'):lines += [f'\n**核对说明：** {e["correction"]}\n']
  if e.get('article'):
   a=e['article'];rel=pathlib.PurePosixPath(a['repositoryPath']).relative_to('docs')
   lines += [f'\n**完整实用指南：** [{a["title"]}]({rel}) · [网站阅读]({a["url"]})\n']
  p=e.get('podcast')
  if p:
   lines += [f'\n**{p["sourceRole"]}：** {p["summary"]}\n',f'[{p["show"]} · {p["episodeTitle"]}]({p["url"]})\n',f'{p["who"]}（{p["role"]}） · feed 日期 {p["date"]} · **{p["timestamp"]}** · {p["speaker"]}。{p["provenance"]}\n']
   if p.get('conflict'):lines += [f'关系披露：{p["conflict"]}\n']
   if p.get('identityEvidence'):lines += [f'身份自述定位：{p["identityEvidence"]["timestamp"]}。\n']
  else:lines += [f'\n**官方补充：** {e["sourceGap"]} 没有编配节目时间戳。\n']
 (R/f'docs/{topic.upper()}.md').write_text('\n'.join(lines).rstrip()+'\n')
lines=['# 节目目录与审阅状态\n',f'节目库观察日期 {meta.get("corpusObservedDate",meta["observedDate"])}；片段引用状态更新 {meta["observedDate"]}。本机节目库共 {len(episodes)} 集，{sum(e["transcriptAvailable"] for e in episodes)} 份字幕可用。目录不是对节目全文的总结。\n','`已引用片段` 只表示阅读并引用了所列时段及相邻上下文；不表示全期完整审阅或听音。`已索引待审阅` 不构成任何内容结论。\n','[项目首页](../README.md) · [Health](HEALTH.md) · [Wealth](WEALTH.md)\n','| 节目 | feed 日期 | 单集 | 状态 / 条目 |','| --- | --- | --- | --- |']
for e in episodes:
 refs='、'.join(f'[{i}]({e["topic"].upper()}.md#{i})' for i in e['entryIds'])
 status={'selected-passages':'已引用片段','indexed-unreviewed':'已索引待审阅','unavailable':'无可用 Apple 字幕'}[e['reviewStatus']]
 title=e['title'].replace('|','/').replace('[','(').replace(']',')')
 lines.append(f'| {e["show"]} | {e["date"]} | [{title}]({e["url"]}) | {status}{" / "+refs if refs else ""} |')
(R/'docs/EPISODES.md').write_text('\n'.join(lines).rstrip()+'\n')
print('Handbooks generated: HEALTH.md, WEALTH.md, EPISODES.md')
(R/'docs/ARTICLES.md').write_text(inventory(catalog()))
