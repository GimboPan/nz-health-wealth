# 在新西兰，好好生活 · NZ Health & Wealth

**给在新西兰生活的中文读者，一份按场景查阅、来源透明、可以共同维护的健康与财富指南。**

[项目统一入口](https://gimbo.co.nz/ideas/nz-health-wealth/) · [打开交互指南](https://gimbo.co.nz/ideas/nz-health-wealth-guide.html) · [专题文章目录](docs/ARTICLES.md) · [Health 专题](docs/HEALTH.md) · [Wealth 专题](docs/WEALTH.md)

看病之前该问谁？续方、转介和资助怎么确认？KiwiSaver、房贷和保险应该先问哪些问题？本项目从 **The Health Hub** 与 **Smart Money** 的本地 Apple 自动字幕出发，把本地长对话整理成中文行动条目，再用主管机构与公共教育资料核对流程、资格及费用。

项目与节目、嘉宾、政府机构没有官方隶属或背书关系。它是一份信息查询与教育工具，未经过独立医疗、法律或财务专业人员逐条审阅。

## 2026年10月25日 Fitness校正与三份就医工具

新增[Healthpoint找服务](docs/guides/healthpoint-find-care.md)、[问诊与结果追踪模板](docs/guides/gp-visit-follow-up.md)、[家属饮酒问题求助](docs/guides/alcohol-family-support.md)。两条新场景以官方补充标明节目缺口；现有等待与沟通条目链接共同模板。

四篇Fitness旧文及原入口保留，已校正确认的错误或过时说法，保留历史背景和每处更新来源。[校正记录](docs/FITNESS-CORRECTIONS.md)与独立校正数据同存GitHub；没有扩大节目听音或全文临床审阅范围。

## 统一目录与Fitness就医资料

[Ideas统一入口](https://gimbo.co.nz/ideas/nz-health-wealth/)分为交互指南与专题文章。新增[新西兰就医资料导读](docs/guides/nz-care-reading.md)（[网站阅读](https://gimbo.co.nz/ideas/nz-health-wealth-care-reading/)），把Fitness里的九章就医指南、Healthpoint使用说明、GP节目整理及酒精与依赖专题串成阅读路线，四篇原文与网址保留。

专题原文和`content/articles.json`是目录的维护入口；GitHub目录与网站目录从同一份清单生成。新增文章时运行同步工具，避免出现只更新一边或统一入口漏链。旧文保留历史资料日期，已确认的重点校正另标2026-10-25；不重新计算节目覆盖或把未复核旧规则当现行规则。

## 2026年10月25日 就医选择补充

新增[GP约不上，今天还有哪些就医选择](docs/guides/gp-access-options.md)（[网站阅读](https://gimbo.co.nz/ideas/nz-health-wealth-gp-access/)）。分别说明Healthline、线上GP、urgent care和Emergency Q的用途、使用步骤、收费示例和适用边界；从现有[当天就医条目](docs/HEALTH.md#same-day)也能进入全文。

v1.1.1扩展原有条目，总量仍为111条，没有新增节目引用。该条公共资料核对于2026-10-25，其他条目保留各自核对日期；价格示例不代表全国统一报价，未实测App或完成独立专业审阅。

## 从这里开始

| 你眼前的事 | 阅读入口 |
| --- | --- |
| 刚到新西兰，找 GP、核对公费资格、需要口译 | [Health：找入口](docs/HEALTH.md#enrol) |
| 今天身体不舒服，不知道从哪里求助 | [Health：分诊与求助](docs/HEALTH.md#healthline) |
| 想弄明白 KiwiSaver 和工资单 | [Wealth：缴费比例](docs/WEALTH.md#kiwi-rate) |
| 家庭现金流、房贷、保险或退休需要重新安排 | [Wealth 专题](docs/WEALTH.md) |
| 想回到节目原文的位置查证 | [全部节目目录与审阅状态](docs/EPISODES.md) |
| 想检查这份指南怎么做出来 | [蒸馏记录](docs/DISTILLATION.md) · [公共资料查核表](docs/SOURCE-CHECKS.md) |

## v1.2.0 包含什么

- **113 条场景指南：Health 56、Wealth 57。** 从就医与健康支持，到家庭现金流、债务、房贷、保险、税务、退休与法律安排。
- **109 条带节目出处和真实说话人时段**，涉及 84 集；另 4 条官方补充明确保留节目缺口。
- **129 个条目公共资料来源页面**，记录查核日期、范围及纠正说明。公共教育建议与现行规则分别标注。
- **725 集公开目录**：717 份字幕可用、8 集无 Apple 字幕标记。每集明确“已引用片段 / 已索引待审阅 / 无可用字幕”。
- 搜索、双专题和分类筛选、场景入口、本地收藏、条目定位、Markdown 导出、目录 CSV 导出、打印。
- 可离线使用的单文件网页；无账号、无追踪、无前端运行依赖。

**v1.0 的“完整”指首版的阅读、引用、维护与发行路径完整。** 717 份字幕是研究底库，其中一组正文精确重复，共 716 份不同正文。已取得、已索引与已阅读是不同状态；本项目没有声称已逐集完整蒸馏或听音复核全部节目。覆盖边界见 [版本说明](docs/RELEASE.md)。

## 一条指南怎样阅读

**场景 → 下一步 → 费用与成本 → 适用边界 → 可复制英文问法 → 节目观点及定位 → 公共资料及核对日期。**

`节目依据` 支持条目的核心经验；`节目背景` 只说明问题从何而来，现行规则另查公共资料。来源标注不是专家认证。节目与官方口径有差异时，会在条目中直接显示。

v1.1.0新增 **25 条**，来自此前未采用的 **24 集**；见 [本轮取舍与来源表](docs/batches/2026-10-21.md)。新增条目查核于 **2026-10-21**，旧条目保留各自日期；节目库文件观察仍截至 2026-10-20。下载的文件是一个时间快照，不会自动更新；政策、费用和资格应回到所列官方入口再次确认。

## 本地使用与开发

要求 Python 3.9+；构建只用标准库。Node 仅用于 JavaScript 语法检查。

```bash
python3 scripts/validate_public.py
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

打开 `http://127.0.0.1:8765`，或双击 `dist/index.html` 离线阅读。收藏保存在当前浏览器；文件地址与 HTTP 地址使用各自的存储空间。

```text
content/entries.json         主要内容入口
content/episodes.json        经过清理的公开节目目录，无原文与本机路径
content/evidence-ledger.json 说话人时段与段落指纹
content/source-checks.json   公共资料核对范围
src/                        暖色编辑风格的静态阅读器
scripts/                    构建、验证、生成专题手册和本机参考库工具
docs/HEALTH.md               GitHub 可直接阅读的健康专题
docs/WEALTH.md               GitHub 可直接阅读的财富专题
docs/EPISODES.md             全部节目清单与审阅状态
```

修改 `content/entries.json` 后：

```bash
python3 scripts/handbooks.py
python3 scripts/report.py
python3 scripts/validate_public.py
python3 scripts/build.py
node --check src/app.js
```

维护方法见 [CONTRIBUTING](CONTRIBUTING.md)、[编辑规范](docs/EDITORIAL.md) 和 [数据结构](docs/ARCHITECTURE.md)。GitHub Actions 会检查公开数据一致性、构建及 JavaScript 语法；有私有原稿的维护者还能核对实际字幕边界。

## 可选：接入自己的本地字幕

公开阅读与构建不需要字幕。研究工具 `corpus.py` 可适配用户自己持有、接口兼容 listen-podcast 的 `apple_transcript.py`。提取器本身与完整字幕不随本仓库分发。

```bash
python3 scripts/corpus.py --show 'The Health Hub' --extractor /path/to/apple_transcript.py --existing-corpus /path/to/transcripts --output private-reference/health
python3 scripts/search_corpus.py private-reference/health/search.sqlite 'continuity'
python3 scripts/validate_evidence.py --inventory private-reference/health/inventory.json --inventory private-reference/wealth/inventory.json
```

只读取 Podcasts 活库的临时副本，复用已有字幕并补取 Apple 字幕。没有字幕就记缺失，不下载音频或自动改用 ASR。节目库范围不保证等于发行方全部历史节目。

## 参与与许可

欢迎提交具体纠错、来源更新、读者场景和带出处的补充。请勿在公开 Issue 上传个人病历、财务档案、账号信息或完整节目字幕。

- 代码：**MIT**，见 [LICENSE](LICENSE)。
- 自行撰写的摘要、说明和界面文字：**CC BY 4.0**，见 [CONTENT-LICENSE.md](CONTENT-LICENSE.md)。
- 原始节目、音频、字幕、第三方标题、商标与链接资料归各自权利人；上述许可不覆盖它们。

[更新记录](CHANGELOG.md) · [当前版本范围与后续路线](docs/RELEASE.md) · [测试记录](docs/QA.md) · [GitHub与网站同步发布](docs/PUBLISHING.md)
