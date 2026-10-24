# GitHub与个人网站同步发布

自2026年10月25日起，正式新增或修改NZ Health & Wealth内容时，GitHub和个人网站共同更新。用户明确要求草稿、研究或暂不发布时，保留相应状态，不进入正式内容。

## 各入口的职责

| 入口 | 职责 |
| --- | --- |
| [Ideas项目文章](https://gimbo.co.nz/ideas/nz-health-wealth/) | 项目的统一公开入口，能够找到交互指南与全部已发布专题文章 |
| [GitHub项目](https://github.com/GimboPan/nz-health-wealth) | 结构化内容、专题原文、来源、代码和版本历史 |
| [交互指南](https://gimbo.co.nz/ideas/nz-health-wealth-guide.html) | 搜索、筛选和查阅场景条目，并进入相关全文 |
| [专题文章目录](ARTICLES.md) | GitHub侧的已发布全文清单，与Ideas入口保持一致 |

## 内容与入口同步

1. 在本仓库修改`content/entries.json`及`docs/guides/`中的专题原文；保留稳定条目ID、真实来源和各条实际核对日期。
2. 从同一份结构化数据重新生成专题手册、来源报告和`dist/index.html`。将网页同步至个人网站的`public/ideas/nz-health-wealth-guide.html`。
3. 新增或修改专题文章时，同步个人网站的文章页面，核对正文、费用、限制、来源链接和日期与GitHub原文一致。维护本仓库`docs/ARTICLES.md`及相关条目的`article`字段。
4. 维护网站`src/pages/ideas/nz-health-wealth.astro`，确保统一入口链接到交互指南和目录中每一篇已发布专题文章。文章与指南也应能返回项目入口；改名或撤下时修正旧链接或安排跳转。
5. 涉及内容版本、数量、来源或范围变化时，同步本仓库元数据、版本记录，以及网站`src/data/nz-health-wealth-release.json`和相关介绍。仅维护说明变更无需虚增内容版本或篇目数量，旧条目核对日期不能一起改新。

## 检查与发布

运行适用于实际改动的检查：

```bash
python3 scripts/handbooks.py
python3 scripts/report.py
python3 scripts/validate_public.py
python3 scripts/build.py
node --check src/app.js
```

网站运行`npm run build`。修改引用时另核节目证据；修改阅读界面时检查桌面与手机。检查公开内容、元数据及发行物不含原始字幕、凭据、私人病历、财务资料或本机路径。

在两个仓库分别提交本次范围内的文件并推送。网站沿用现有main分支自动部署；涉及内容发行版本时同步相应GitHub发行物。

完成回报前，确认：

- GitHub已包含本次内容且相关检查通过。
- 网站部署成功，实际公开页面显示本次修改；不能用本地构建或部署排队状态代替上线确认。
- 从Ideas项目文章能进入交互指南和全部已发布专题文章，新文章的往返链接有效。
- 两边正文、来源、日期及版本信息一致；如只有一边成功，明确报告部分完成并继续修复。

本流程不调整小红书发布队列、排期或批准素材，也不扩大到其他项目或私人资料。
