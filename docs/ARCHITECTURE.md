# 数据与工程结构

## 两层工程

**公开层**：结构化条目、元数据、前端代码和文档。Python 构建为单个 HTML；零前端运行依赖、无数据库服务、无外部资源请求。

**本地参考层**：Podcasts 数据库临时副本、现有 Apple 字幕与补取稿、库存 CSV/JSON、SHA-256、SQLite FTS5 段落索引。全部排除在公开仓库之外。

```text
Apple Podcasts 本地库副本
  → 节目单集清单
  → 现有字幕 / Apple TTML 补缺
  → 正文密度检查 + 台账
  → 带时间戳 FTS5 索引
  → 人工选题、阅读上下文、查官方资料
  → content/entries.json
  → scripts/build.py
  → dist/index.html
```

## 主要字段

| 字段 | 意义 |
| --- | --- |
| `id` | 稳定英文 slug，用于定位链接和收藏 |
| `topic` | health / wealth |
| `category`、`tags` | 分类及搜索同义词 |
| `title`、`summary` | 一条问题及一句提示 |
| `steps`、`cost`、`limit` | 编辑动作、成本和条件 |
| `english` | 编辑写的英文询问句 |
| `official`、`sources`、`checked` | 公共资料摘要、链接和查核日期 |
| `podcast` | 嘉宾、节目、feed 日期、ID、真实说话人时段、段落 SHA-256、摘要、关系、来源用途和核验方式 |
| `status` | 本次核对 / 节目经验，指公共资料查核状态而非整条专业审核 |
| `entryType`、`sourceGap` | 官方补充须明确节目缺口；不能编造来源 |
| `correction` | 对节目或旧稿说法的收窄、补充或纠正 |

收藏保存于浏览器 localStorage。移动、改名或更换协议可能影响浏览器对收藏所在源的判断。数据不上传。

## 参考库接入

`corpus.py` 是适配器，不复制外部提取器代码。用户指定自己持有的 listen-podcast `apple_transcript.py`。仅匹配指定节目；复制 SQLite/WAL 后读；按 episode ID 复用，缺字幕标记不发请求，TTML 解析或低密度失败要记账，不改走音频。索引查询结果供阅读上下文，不能从检索片段直接拼成未经核实的医学或财务结论。

## 本次范围

Health Hub 366 份 + Smart Money 351 份 = 717 份可用字幕，约 517.6 万英文词，按本地时长字段合计约 472.4 小时。词数采用正文空白分词。八集无字幕标记；不是“所有节目都成功”。这些数量是抓取与文件检查结果，不是人工审阅覆盖量。

## 公开审计链（v1.0）

`topic-taxonomy.json` + 本地库存 → `map_topics.py` → `research-map.json`（字面候选与重复审计）；人工选取段落并查资料 → `entries.json` + `evidence-ledger.json` → `validate_evidence.py` 对私有原稿核查起止、说话人及段落哈希 → `report.py` 生成蒸馏记录与来源查核表 → `build.py`。

84 条节目引用对应 79 个不同主段落及 60 集；同一段可支持不同问题，不把重复引用算成独立证据。另有一处身份自述证据。公开账本只有定位和哈希，不含字幕原文。717 份文件中发现一组精确重复，故为 716 份不同正文。

## 公开阅读与目录

`episodes.json` 是由私有库存清理生成的 725 集公开元数据，只保留节目、单集 ID、feed 日期、标题、Apple 单集链接、字幕可用性和选定片段引用状态。`handbooks.py` 从同一份条目生成 GitHub 可读手册与目录；`validate_public.py` 不需要私有原稿，核对条目、目录和账本的交叉引用。
