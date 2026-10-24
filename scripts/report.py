"""Create a public editorial audit trail without distributing transcript text."""
import collections,json,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
entries=json.loads((R/'content/entries.json').read_text());meta=json.loads((R/'content/meta.json').read_text());research=json.loads((R/'content/research-map.json').read_text())
citations=[e['podcast'] for e in entries if e['podcast']]
counts=collections.Counter(e['topic'] for e in entries)
supplements=[e for e in entries if not e['podcast']]
lines=[f'# 系统蒸馏记录 · v{meta["version"]}',f'\n观察日期：{meta["observedDate"]}（新西兰时间）。\n',
 f'当前共 {len(entries)} 条：Health {counts["health"]}、Wealth {counts["wealth"]}。其中 {len(citations)} 条带节目时段，涉及 {len({p["eid"] for p in citations})} 集中的 {len({p["evidenceId"] for p in citations})} 个不同主引用段落；另有 {len(supplements)} 条官方补充。',
 f'\n相对 v0.1.0 的 28 条，累计新增 {len(entries)-28} 条。v1.0 的完整范围是高频场景指南、公开节目目录及可维护的开源工程；不表示已完整审阅每一期。\n',
 '## 蒸馏流程与本轮范围\n',
 '- v1.1.0 从此前未引用的 24 集选取 25 个主引用段落，新增 Health 12 条、Wealth 13 条；本轮表与取舍见 [2026-10-21 批次](batches/2026-10-21.md)。',
 '- v1.1.1 于2026-10-25扩展same-day条目，补充Healthline、线上GP、urgent care、Emergency Q及完整实用指南；新增服务信息只依据公开资料，不新增节目引用。',
 '- 节目库文件观察仍截至2026-10-20；v1.1.0新增条目查核于2026-10-21，same-day本次更新为2026-10-25，其余条目保留各自日期。',
 '- 前序版本已对 717 份可用字幕做正文关键词候选扫描，按正文精确去重，并把明显商业广告模式从候选计数中排除。',
 '- 从候选与既有蒸馏中选择场景，阅读引用发言及前后上下文，不靠标题猜内容。',
 '- 对时间戳、说话人标签及段落 SHA-256 进行机械对照；该检查确认可定位，不证明每个观点正确。',
 '- 对政策、资助、费用、税务及法律条件另查主管机构资料；教育性建议与法律硬规则分别表述。',
 '- 保留节目背景与直接依据的区别；核对发现的差异直接显示在条目。\n',
 '## 全库扫描边界\n','| 专题 | 字幕文件 | 不同正文 | 扫描段落 | 广告提示模式排除段落 |','| --- | ---: | ---: | ---: | ---: |']
for topic,r in research['topics'].items():lines.append(f"| {topic} | {r['availableFiles']} | {r['distinctBodies']} | {r['scannedBlocks']} | {r['adPatternExcludedBlocks']} |")
lines+=['\n主题匹配是字面检索候选，不是对全部节目的语义总结。广告模式排除也不等于广告人工审计。Health Hub 的 1000625861478 与 1000625815897 字幕正文完全相同，不当作两份独立证据。\n',
 '## 来源性质\n']
for role,n in collections.Counter(p['sourceRole'] for p in citations).items():lines.append(f'- {role}：{n} 条。')
for e in supplements:lines.append(f'- 官方补充 **{e["title"]}**：{e["sourceGap"]}')
lines+=['\n## 累计收窄或纠正记录\n']
for e in entries:
 if e.get('correction'):lines.append(f'- **{e["title"]}**：{e["correction"]}')
lines+=['\n## 全部条目的节目定位\n','| 专题 / 条目 | 单集 feed 日期 | 嘉宾 / 时段 | 来源用途 |','| --- | --- | --- | --- |']
for e in entries:
 p=e['podcast'];title=e['title'].replace('|','/')
 if p:lines.append(f"| {e['topic']} / {title} | [{p['date']} · {p['eid']}]({p['url']}) | {p['who']} / {p['timestamp']} | {p['sourceRole']} |")
 else:lines.append(f"| {e['topic']} / {title} | 官方补充 | 节目未覆盖，未编造时段 | 官方补充 |")
lines+=['\n## 还没有完成的事\n',
 '没有逐集通读或听音复核全部 717 份字幕；没有完成独立临床、法律或财务专业审阅。节目标题可能错位，feed 日期可能回填，自动字幕也可能误认词语与说话人。',
 '\n主引用时间范围是说话人段落边界，不能当作中文摘要逐词与原音精确对齐。新出现的临床建议只保留寻求评估或沟通的动作，不把节目个案转成个体治疗方案。',
 '\n完整字幕、私有台账和 SQLite 只留本地，不进入公开工程。公开发行只含自行撰写的指南、节目定位、公开目录及程序；发布状态见 README 和版本记录。']
(R/'docs/DISTILLATION.md').write_text('\n'.join(lines).rstrip()+'\n')
sources={}
for e in entries:
 for s in e['sources']:
  x=sources.setdefault(s['url'],dict(label=s['label'],checked=s.get('checked'),method=s.get('method'),entries=[]))
  x['entries'].append(dict(id=e['id'],title=e['title'],claim=e['official'],checked=s['checked'],method=s.get('method')))
  x['checked']=max(x['checked'],s['checked'])
  x['checkedDates']=sorted({v['checked'] for v in x['entries']})
data=[dict(url=url,**v) for url,v in sources.items()]
(R/'content/source-checks.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
text=['# 公共资料查核记录（检索级）\n',f'观察日期：{meta["observedDate"]}。列出 {len(data)} 个不同来源页面，范围以关联条目的公共资料摘要为准。部分官网直接抓取受限，使用工具返回的官方正文或检索摘录核对；未把“链接存在”当作整个条目已获专业验证。\n']
for s in data:
 text.append(f"## [{s['label']}]({s['url']})\n\n最近查核日期：{s['checked']}；各条目实际查核日期见下。\n")
 for e in s['entries']:text.append(f"- **{e['title']}**（{e['checked']}）：{e['claim']}")
 text.append('')
(R/'docs/SOURCE-CHECKS.md').write_text('\n'.join(text).rstrip()+'\n')
print(f'Reports built: {len(entries)} entries, {len(data)} public source pages.')
