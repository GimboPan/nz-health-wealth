# 系统蒸馏记录 · v1.1.2

观察日期：2026-10-25（新西兰时间）。

当前共 111 条：Health 54、Wealth 57。其中 109 条带节目时段，涉及 84 集中的 104 个不同主引用段落；另有 2 条官方补充。

相对 v0.1.0 的 28 条，累计新增 83 条。v1.0 的完整范围是高频场景指南、公开节目目录及可维护的开源工程；不表示已完整审阅每一期。

## 蒸馏流程与本轮范围

- v1.1.0 从此前未引用的 24 集选取 25 个主引用段落，新增 Health 12 条、Wealth 13 条；本轮表与取舍见 [2026-10-21 批次](batches/2026-10-21.md)。
- v1.1.1 于2026-10-25扩展same-day条目，补充Healthline、线上GP、urgent care、Emergency Q及完整实用指南；新增服务信息只依据公开资料，不新增节目引用。
- 节目库文件观察仍截至2026-10-20；v1.1.0新增条目查核于2026-10-21，same-day本次更新为2026-10-25，其余条目保留各自日期。
- 前序版本已对 717 份可用字幕做正文关键词候选扫描，按正文精确去重，并把明显商业广告模式从候选计数中排除。
- 从候选与既有蒸馏中选择场景，阅读引用发言及前后上下文，不靠标题猜内容。
- 对时间戳、说话人标签及段落 SHA-256 进行机械对照；该检查确认可定位，不证明每个观点正确。
- 对政策、资助、费用、税务及法律条件另查主管机构资料；教育性建议与法律硬规则分别表述。
- 保留节目背景与直接依据的区别；核对发现的差异直接显示在条目。

## 全库扫描边界

| 专题 | 字幕文件 | 不同正文 | 扫描段落 | 广告提示模式排除段落 |
| --- | ---: | ---: | ---: | ---: |
| health | 366 | 365 | 63176 | 13 |
| wealth | 351 | 351 | 48862 | 44 |

主题匹配是字面检索候选，不是对全部节目的语义总结。广告模式排除也不等于广告人工审计。Health Hub 的 1000625861478 与 1000625815897 字幕正文完全相同，不当作两份独立证据。

## 来源性质

- 节目背景：39 条。
- 节目依据：70 条。
- 官方补充 **先核对公费资格，再问项目费用**：已审阅的节目段落未覆盖签证与完整公费资格；本条仅按官方资料补充。
- 官方补充 **预约时，就把语言需要说出来**：已审阅的节目段落未提供口译安排依据；本条仅按官方资料补充。

## 累计收窄或纠正记录

- **GP约不上，今天还有哪些就医选择**：2026-10-25补充就医入口和费用：电话健康咨询、线上医生问诊、实体urgent care和地点比较工具分别使用。Emergency Q不提供walk-in预约，也不是全国完整目录。价格仅是特定提供者示例，实际按资格和就诊情况确认。
- **长期药快用完，提前联系开方团队**：处方有效期与一次配药数量是两回事。节目背景不提供新的 12 个月规则。
- **带状疱疹疫苗：65 岁窗口之外，还有特定条件**：“只有 65 岁才资助”过于绝对；某些免疫受损人群也有资助路径。
- **助听器补贴：让听力师分清你走哪套资助**：节目中的“每个居民都可领取”缺少资格条件，不能直接采用。
- **不要把酒当作助眠办法**：节目中口头估计的酒量不是个体适用的安全阈值；本条采用官方“不用酒助眠”的指引。
- **更年期相关困扰，把症状和问题带去谈**：该嘉宾在 01:27 明确说自己不是医学医生；“Dr”在此指博士头衔。
- **想看物理治疗，先问能否直接预约**：节目以旧 DHB 体系概括公立转介；当前部分地方项目接受自我转介，不能视为全国统一规则。
- **“专业渠道”标签，不等于疗效获官方认证**：节目中的渠道品质评价没有证明所有同类产品的疗效；不把它转换成购买建议。
- **投保、续保或情况改变，重新确认披露内容**：既往情况能否承保取决于具体保单和核保结果，不能照节目泛称一律不保。
- **收入变化后，重算 PIR 再通知基金**：不是退休后直接挑最低税率；应使用 IRD 的现行计算工具。
- **卖股票获利，不只“职业交易员”才可能缴税**：“不是 trader 就不纳税”不准确；IRD 还看买入时的主要目的等事实。
- **存款保障，按每人每家机构合并核对**：节目把保障说成每个账户；官方口径是每位存款人、每家存款机构。
- **收到裁员提议，先分清提议、反馈与最终决定**：应问与变更相关的信息；节目不能替代对保密、隐私与信息披露条件的法律判断。
- **诊所和家中血压不同，把记录带回去讨论**：节目中的正常个案不能作为自行排除高血压或停药的依据。
- **术后回工作和运动，先拿到个人恢复安排**：不同手术的限制并不相同；节目个案时间不能代替出院医嘱。
- **担心跌倒，查本地力量与平衡支持**：节目赞同某项测试“有数据”，不等于它能给个人预测寿命。
- **比较包装食品，先看同一种计量单位**：节目中的统一糖分好坏阈值和“一定有标签”概括，不适合推广到所有食品。
- **查信用记录时，先确认事实与错误**：该时段发言者是来电者，不能因单集标题而归给 Martin Hawes。
- **严重财务困难提款，先向 provider 确认材料**：“65 岁前取不了”需要限定；法律与 IRD 列有符合条件的提前提款路径。
- **“免费立遗嘱”，还要问谁执行、以后如何收费**：不能概括所有免费服务都强制指定执行人；应逐家核对合同。
- **雇主缴款少于工资单比例，先查 ESCT**：节目谈到取消税的设想；此处仅记录截至核对日的 IRD 现行处理。
- **定期投入是一种安排，不是稳赚或抄底保证**：节目中“现在是买入机会”的时点意见不能转写成今天的建议。
- **NZ Super 与 KiwiSaver 分开核对资格**：选举主张、未来设想和已实施规则要分开；不能把“67 岁”当作截至核对日的统一现行年龄。
- **流感针每年重新核对，先问资助资格**：官网页面中的旧视频文字与 2026 年正文资助清单存在差别；本条采用当年正文，不沿用旧年龄概括。
- **用 AI 整理问诊问题，结果仍要核实**：不采用节目其他段落中未经核实的网络错误比例，也不将专用或付费 AI 写成无错误保证。
- **噪音防护先减少暴露，再选合适护具**：节目给的设备音量百分比口诀不能取代实际噪音风险评估。
- **宫颈筛查先核对适用方式，再问是否免费**：不把“国家筛查项目”理解为人人免费，也不把节目建议的健康回顾频率当成统一筛查间隔。
- **怀疑乳糜泻，先问检测再自行戒麸质**：不采用同集其他段落中把疾病与单一祖籍联系的概括，也不把一般营养讨论当成诊断。
- **旅行打乱排便习惯，先恢复适合自己的节奏**：不把固定补水量或无限增加纤维推广为普遍处方。
- **耳堵或听力变化，先确认是否真是耳垢**：舍弃节目里的自配滴耳液与“十次有九次有效”说法，改为先评估原因和个人禁忌。
- **年报酬达到 20 万，解雇保护要单独核对**：门槛是 200,000 或以上；不是所有 PG 均排除，也不是公司车、雇主 KiwiSaver 等所有福利一律计入。过渡及书面恢复保护另有条件。
- **看退休村，先算入住、居住和退出三笔账**：该时段是来电者；其金额、跨境居住与养老金个案不能改写成一般规则。
- **房贷 cashback，先读返还条件再比较优惠**：旧促销不是现行报价，返还期和算法也不能从某家银行推广到全部银行。

## 全部条目的节目定位

| 专题 / 条目 | 单集 feed 日期 | 嘉宾 / 时段 | 来源用途 |
| --- | --- | --- | --- |
| health / 情况危急时，先拨 111 | [2023-10-01 · 1000629833365](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000629833365) | Dr John Cameron / 20:30–20:51 | 节目背景 |
| health / 拿不准去哪看，先问 Healthline | [2026-08-16 · 1000783555883](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000783555883) | Dr Bryan Betty / 12:32–14:06 | 节目背景 |
| health / GP约不上，今天还有哪些就医选择 | [2026-01-25 · 1000746529862](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000746529862) | Dr Bryan Betty / 21:52–22:02 | 节目依据 |
| health / Enrol：先把自己注册进一家诊所 | [2026-03-22 · 1000756542337](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000756542337) | Dr John Cameron / 08:01–08:12 | 节目依据 |
| health / 听到 closed books，继续问可选路径 | [2026-03-22 · 1000756542337](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000756542337) | Dr John Cameron / 14:19–14:35 | 节目依据 |
| health / 慢性或复杂问题，尽量连续看同一位医生 | [2026-08-16 · 1000783555883](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000783555883) | Dr Bryan Betty / 05:57–06:55 | 节目依据 |
| health / 先核对公费资格，再问项目费用 | 官方补充 | 节目未覆盖，未编造时段 | 官方补充 |
| health / 取药前，问清处方费和额外费用 | [2023-04-16 · 1000609126035](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000609126035) | Niki Bezzant / 16:51–16:56 | 节目背景 |
| health / 意外受伤，问医疗提供者能否申请 ACC | [2026-01-25 · 1000746529862](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000746529862) | Dr Bryan Betty / 35:47–36:49 | 节目依据 |
| health / 进药房时，明确找 pharmacist | [2025-05-04 · 1000706109816](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000706109816) | Claire Turnbull / 06:36–08:19 | 节目依据 |
| health / 把全部用药带给药师一起核对 | [2022-11-30 · 1000588038174](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000588038174) | Dr John Cameron / 25:15–25:46 | 节目依据 |
| health / 长期药快用完，提前联系开方团队 | [2026-08-16 · 1000783555883](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000783555883) | Dr Bryan Betty / 05:57–06:55 | 节目背景 |
| health / 需要专科时，先问评估和转介路径 | [2025-12-14 · 1000741184600](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000741184600) | Dr Michel Neeff / 23:30–23:53 | 节目依据 |
| health / 转介后，把回信和复评节点记下来 | [2025-01-26 · 1000685475276](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000685475276) | Dr John Cameron / 14:48–15:13 | 节目依据 |
| health / 想找心理支持，先问诊所有没有 HIP | [2026-02-15 · 1000749791420](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000749791420) | Matt Doocey / 20:41–21:37 | 节目背景 |
| health / 预约时，就把语言需要说出来 | 官方补充 | 节目未覆盖，未编造时段 | 官方补充 |
| health / 肠癌筛查：56 岁门槛有地区差异 | [2026-10-11 · 1000795210535](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000795210535) | Dr John Cameron / 07:19–08:56 | 节目背景 |
| health / 乳腺筛查：年龄扩展要查出生日期和地区 | [2025-10-19 · 1000732487624](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000732487624) | Dr Bryan Betty / 05:36–06:44 | 节目背景 |
| wealth / 应急的钱，先留在方便取用的地方 | [2026-05-31 · 1000770397790](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000770397790) | Nick Crawford / 08:40–09:30 | 节目依据 |
| wealth / 买产品前，先写下用钱的时间 | [2026-10-04 · 1000793052879](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000793052879) | Amanda Morrall / 07:34–08:18 | 节目依据 |
| wealth / 先把每笔债的总成本列清楚 | [2025-11-23 · 1000737960798](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000737960798) | Martin Hawes / 23:04–23:51 | 节目依据 |
| wealth / 和伴侣谈钱，先把事实摆上桌 | [2026-08-30 · 1000786738733](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000786738733) | Nick Crawford / 04:04–04:24 | 节目依据 |
| wealth / KiwiSaver：先核对工资单上的比例 | [2025-05-25 · 1000709764980](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000709764980) | Tim Beveridge / 00:31–02:27 | 节目背景 |
| wealth / 政府 KiwiSaver 补贴，按当年资格核对 | [2025-05-25 · 1000709764980](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000709764980) | Tim Beveridge / 00:31–02:27 | 节目背景 |
| wealth / 查自己在哪个基金，再比较是否合适 | [2026-10-04 · 1000793052879](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000793052879) | Amanda Morrall / 30:41–32:04 | 节目依据 |
| wealth / 首次买房提款，签约前先问 provider | [2024-04-14 · 1000652423942](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000652423942) | Andrew Bascand / 20:56–22:10 | 节目背景 |
| wealth / 投资前，独立查证对方身份和付款信息 | [2025-01-19 · 1000684544184](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000684544184) | Amanda Morrall / 07:48–09:58 | 节目依据 |
| wealth / 让 AI 帮你列问题，结论回到原始来源 | [2026-08-09 · 1000781158639](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000781158639) | Amanda Morrall / 03:53–04:50 | 节目依据 |
| health / 孩子的牙科，要单独确认是否已注册 | [2020-09-13 · 1000491070393](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000491070393) | Dr John Cameron / 03:56–04:33 | 节目依据 |
| health / 带状疱疹疫苗：65 岁窗口之外，还有特定条件 | [2024-09-08 · 1000668755872](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000668755872) | Dr John Cameron / 33:34–33:43 | 节目背景 |
| health / 助听器补贴：让听力师分清你走哪套资助 | [2024-03-04 · 1000647868800](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000647868800) | Lesleigh Smith / 20:59–21:22 | 节目背景 |
| health / CPAP 用不惯，回到开机与治疗团队排查 | [2026-06-07 · 1000771516513](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000771516513) | Alex Bartle / 23:42–24:01 | 节目依据 |
| health / 睡不好，先记录规律与白天影响 | [2026-06-07 · 1000771516513](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000771516513) | Alex Bartle / 38:42–39:17 | 节目依据 |
| health / 不要把酒当作助眠办法 | [2026-06-07 · 1000771516513](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000771516513) | Alex Bartle / 06:39–07:12 | 节目依据 |
| health / 更年期相关困扰，把症状和问题带去谈 | [2025-08-03 · 1000720464905](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000720464905) | Sola Freeman / 23:00–23:59 | 节目依据 |
| health / 想看物理治疗，先问能否直接预约 | [2025-06-22 · 1000714019451](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000714019451) | Caitlin Fris / 39:53–40:16 | 节目依据 |
| health / 骨密度下降，先评估再选力量训练 | [2026-08-02 · 1000779490490](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000779490490) | Greg Pain / 06:39–07:18 | 节目依据 |
| health / 有症状时，不要等到免费筛查年龄 | [2023-02-26 · 1000601607558](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000601607558) | Dr John Cameron / 28:12–28:25 | 节目依据 |
| health / “专业渠道”标签，不等于疗效获官方认证 | [2025-05-04 · 1000706109816](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000706109816) | Claire Turnbull / 27:25–27:57 | 节目背景 |
| health / 不同意 ACC 决定，先看决定信和复核期限 | [2024-06-24 · 1000659998404](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000659998404) | Tim Beveridge / 29:13–29:24 | 节目背景 |
| health / 漏尿或盆底困扰，可以直接开口求助 | [2025-06-22 · 1000714019451](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000714019451) | Caitlin Fris / 06:48–07:20 | 节目依据 |
| health / 找医生时，核对登记与当前执业状态 | [2026-03-22 · 1000756542337](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000756542337) | Dr John Cameron / 14:41–15:16 | 节目依据 |
| wealth / 固定还是浮动，先比较预算与合同限制 | [2025-11-30 · 1000738948055](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000738948055) | Lisa Dudson / 25:12–25:21 | 节目依据 |
| wealth / 转贷或提前重签，先要一份完整费用表 | [2024-10-27 · 1000674589898](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000674589898) | Amanda Morrall / 10:19–10:46 | 节目依据 |
| wealth / 房贷分段到期，是一个需要讨论的风险安排 | [2025-11-30 · 1000738948055](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000738948055) | Lisa Dudson / 27:12–27:55 | 节目依据 |
| wealth / 循环房贷的灵活性，也可能让本金一直降不下去 | [2025-11-30 · 1000738948055](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000738948055) | Lisa Dudson / 25:52–26:51 | 节目依据 |
| wealth / 保费上涨，先一起看 excess 和应急金 | [2025-08-31 · 1000724230207](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000724230207) | Shamubeel Eaqub / 06:52–07:12 | 节目依据 |
| wealth / 投保、续保或情况改变，重新确认披露内容 | [2021-12-05 · 1000543979014](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000543979014) | Amanda Morrall / 25:54–26:18 | 节目依据 |
| wealth / 收入变化后，重算 PIR 再通知基金 | [2024-06-17 · 1000659210173](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000659210173) | Chris Di Leva / 22:09–23:06 | 节目依据 |
| wealth / 海外股票，先核对 FIF 与适用例外 | [2025-04-27 · 1000705101319](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000705101319) | Chris Di Leva / 22:39–25:37 | 节目背景 |
| wealth / 卖股票获利，不只“职业交易员”才可能缴税 | [2025-04-27 · 1000705101319](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000705101319) | Chris Di Leva / 22:39–25:37 | 节目背景 |
| wealth / 存款保障，按每人每家机构合并核对 | [2025-06-08 · 1000711974718](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000711974718) | Rupert Carlyon / 29:13–29:43 | 节目背景 |
| wealth / 多个产品，不一定代表真正分散 | [2026-08-02 · 1000779494615](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000779494615) | Rupert Carlyon / 05:44–06:04 | 节目依据 |
| wealth / 比较基金，把费用看成长期的一部分 | [2026-08-09 · 1000781158639](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000781158639) | Amanda Morrall / 30:52–32:26 | 节目依据 |
| wealth / 退休需要多少钱，先写自己的预算 | [2025-07-06 · 1000715955133](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000715955133) | Martin Hawes / 34:47–35:35 | 节目依据 |
| wealth / 把退休储蓄转换成收入，先做情景比较 | [2025-03-16 · 1000699340795](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000699340795) | Martin Hawes / 04:23–05:48 | 节目依据 |
| wealth / 到 65 岁，不代表必须一次取走 KiwiSaver | [2024-06-17 · 1000659210173](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000659210173) | Chris Di Leva / 19:49–21:43 | 节目依据 |
| wealth / 现金流吃紧，先查 savings suspension 的条件与代价 | [2025-03-30 · 1000701420289](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000701420289) | Amanda Morrall / 39:38–40:00 | 节目依据 |
| wealth / 找财务顾问，先问他如何收费与受谁委托 | [2025-01-19 · 1000684544184](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000684544184) | Amanda Morrall / 07:48–09:58 | 节目依据 |
| wealth / 答应做 trustee 前，先了解持续责任 | [2025-12-21 · 1000742166628](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000742166628) | Janet Xuccoa / 08:36–09:00 | 节目依据 |
| wealth / 趁能作决定时，了解 EPA 的安排 | [2025-03-16 · 1000699340795](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000699340795) | Martin Hawes / 04:23–05:48 | 节目背景 |
| wealth / 关系财产协议，不只要写下来 | [2026-07-12 · 1000776439356](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000776439356) | Sharon Chandra / 06:10–06:39 | 节目依据 |
| wealth / 收到裁员提议，先分清提议、反馈与最终决定 | [2025-11-02 · 1000734760155](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000734760155) | Max Whitehead / 24:31–25:07 | 节目背景 |
| health / 诊所和家中血压不同，把记录带回去讨论 | [2024-07-14 · 1000662148578](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000662148578) | Dr John Cameron / 19:02–19:31 | 节目依据 |
| health / 皮肤出现新变化，预约时就说明变化 | [2026-10-11 · 1000795210535](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000795210535) | Dr John Cameron / 13:18–13:37 | 节目依据 |
| health / 营养建议互相打架，回到整体饮食与可靠资料 | [2026-09-20 · 1000790749124](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000790749124) | Julia Sekula / 31:50–33:12 | 节目依据 |
| health / 术后回工作和运动，先拿到个人恢复安排 | [2026-07-12 · 1000776432059](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000776432059) | Alex Flint / 12:55–14:27 | 节目背景 |
| health / 担心跌倒，查本地力量与平衡支持 | [2026-07-12 · 1000776432059](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000776432059) | Alex Flint / 23:33–24:32 | 节目背景 |
| health / 耳鸣或听力影响生活，先把问题评估清楚 | [2026-08-30 · 1000786735776](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000786735776) | Dr Michel Neeff / 36:21–37:10 | 节目依据 |
| health / 对方案仍有疑问，可以询问第二意见的路径 | [2026-06-28 · 1000774525085](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000774525085) | Dr Michel Neeff / 33:44–33:57 | 节目背景 |
| health / 比较包装食品，先看同一种计量单位 | [2025-02-09 · 1000690480622](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000690480622) | 节目讨论（说话人身份未确认） / 23:55–24:04 | 节目背景 |
| health / 想减少饮酒，先评估是否需要医疗支持 | [2019-07-21 · 1000444956571](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000444956571) | Margo Regan / 07:02–07:15 | 节目依据 |
| health / 选远程问诊时，把记录与后续衔接问清 | [2026-03-22 · 1000756542337](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000756542337) | Dr John Cameron / 09:46–10:28 | 节目依据 |
| wealth / 财务压力大，可以先找免费保密的预算支持 | [2020-04-12 · 1000471224075](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000471224075) | Tom Hartmann / 28:26–30:13 | 节目依据 |
| wealth / 查信用记录时，先确认事实与错误 | [2020-09-06 · 1000490228039](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000490228039) | 节目来电者 / 26:40–27:28 | 节目背景 |
| wealth / 先买后付，也要放进同一张还款日历 | [2025-07-13 · 1000717020481](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000717020481) | Hannah McQueen / 25:32–26:00 | 节目依据 |
| wealth / 严重财务困难提款，先向 provider 确认材料 | [2026-10-11 · 1000795214281](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000795214281) | Nathan Stanners / 32:32–32:52 | 节目背景 |
| wealth / 准备遗嘱，先把意愿、执行人和复杂情况理清 | [2026-04-19 · 1000762214612](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000762214612) | Janet Xuccoa / 31:27–32:37 | 节目依据 |
| wealth / “免费立遗嘱”，还要问谁执行、以后如何收费 | [2026-08-23 · 1000785194456](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000785194456) | Tim Beveridge / 33:16–33:28 | 节目背景 |
| wealth / 收入中断时，先找家庭预算的缺口 | [2026-01-25 · 1000746534072](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000746534072) | Martin Hawes / 10:25–11:23 | 节目依据 |
| wealth / 租房时，别把房东保险当作自己的物品保障 | [2025-08-31 · 1000724230207](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000724230207) | Shamubeel Eaqub / 20:56–21:15 | 节目背景 |
| wealth / 雇主缴款少于工资单比例，先查 ESCT | [2026-06-22 · 1000773657652](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000773657652) | Nathan Stanners / 22:23–22:48 | 节目依据 |
| wealth / 已经转钱或泄露资料，立即联系自己的银行 | [2023-09-24 · 1000628997972](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000628997972) | Ashley Kai Fong / 08:08–08:39 | 节目背景 |
| wealth / 定期投入是一种安排，不是稳赚或抄底保证 | [2025-04-06 · 1000702356826](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000702356826) | Lisa Dudson / 17:38–18:30 | 节目依据 |
| wealth / 预计还不上贷款，尽早书面联系放款人 | [2023-09-24 · 1000628997972](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000628997972) | Martin King / 02:23–02:58 | 节目背景 |
| wealth / NZ Super 与 KiwiSaver 分开核对资格 | [2026-10-11 · 1000795214281](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000795214281) | 节目来电者 / 13:08–13:28 | 节目背景 |
| health / 流感针每年重新核对，先问资助资格 | [2026-09-13 · 1000789258195](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000789258195) | Dr John Cameron / 22:06–22:19 | 节目依据 |
| health / 用 AI 整理问诊问题，结果仍要核实 | [2026-03-29 · 1000757994005](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000757994005) | Dr Bryan Betty / 05:00–05:52 | 节目依据 |
| health / 噪音防护先减少暴露，再选合适护具 | [2025-09-21 · 1000727698046](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000727698046) | Dr Michel Neeff / 07:53–09:32 | 节目依据 |
| health / 宫颈筛查先核对适用方式，再问是否免费 | [2025-03-16 · 1000699338528](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000699338528) | Dr John Cameron / 12:21–12:55 | 节目背景 |
| health / HPV 疫苗也关乎男性，别只想到宫颈 | [2024-02-18 · 1000645795581](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000645795581) | Dr John Cameron / 11:43–12:25 | 节目背景 |
| health / 找心理治疗时，同时问资质、方式和是否合适 | [2021-08-08 · 1000531361930](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000531361930) | Kyle MacDonald / 16:43–18:11 | 节目依据 |
| health / 怀疑乳糜泻，先问检测再自行戒麸质 | [2026-04-26 · 1000763634255](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000763634255) | Claire Turnbull / 04:10–05:21 | 节目背景 |
| health / 孩子未满 14 岁，仍要问清哪些项目免费 | [2025-08-10 · 1000721351245](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000721351245) | Sir Ashley Bloomfield / 16:22–17:13 | 节目背景 |
| health / 突然新增飞蚊或闪光，当天寻求眼部评估 | [2022-11-13 · 1000589517708](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000589517708) | Philip Walsh / 09:03–09:56 | 节目依据 |
| health / 旅行打乱排便习惯，先恢复适合自己的节奏 | [2025-07-06 · 1000715951612](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000715951612) | Claire Turnbull / 24:55–25:53 | 节目依据 |
| health / 吃药后昏沉，开车前先核对影响 | [2026-04-12 · 1000760898781](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000760898781) | Dr Alex Bartle / 20:19–20:26 | 节目背景 |
| health / 耳堵或听力变化，先确认是否真是耳垢 | [2024-10-20 · 1000673715924](https://podcasts.apple.com/nz/podcast/id1444362063?i=1000673715924) | Dr John Cameron / 40:12–40:33 | 节目背景 |
| wealth / 签工作合同前，带走阅读并提出问题 | [2026-07-05 · 1000775500235](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000775500235) | Sylvie Thrush Marsh / 08:48–09:35 | 节目依据 |
| wealth / 没有拿到书面合同，也不要直接放弃员工权利 | [2026-09-20 · 1000790752666](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000790752666) | Sylvie Thrush Marsh / 14:50–15:36 | 节目依据 |
| wealth / 年报酬达到 20 万，解雇保护要单独核对 | [2026-09-20 · 1000790752666](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000790752666) | Sylvie Thrush Marsh / 06:28–07:21 | 节目背景 |
| wealth / 看退休村，先算入住、居住和退出三笔账 | [2026-05-10 · 1000767023163](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000767023163) | 节目来电者 / 25:13–26:17 | 节目背景 |
| wealth / 申请长期照护补助，先分清需求评估与财务评估 | [2026-02-08 · 1000748728504](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000748728504) | Janet Xuccoa / 06:20–08:11 | 节目依据 |
| wealth / 替家人担保前，问清最坏可能承担多少 | [2026-06-07 · 1000771520201](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000771520201) | Janet Xuccoa / 38:32–39:10 | 节目依据 |
| wealth / 房贷 cashback，先读返还条件再比较优惠 | [2020-07-26 · 1000486343273](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000486343273) | Carissa Fairbrother / 21:28–22:10 | 节目背景 |
| wealth / 只还息可以缓解眼前月供，本金仍然在 | [2023-07-02 · 1000619067115](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000619067115) | Antonia Watson / 07:10–08:24 | 节目依据 |
| wealth / 让孩子练习花、存和等待，规则先谈好 | [2025-07-20 · 1000718129557](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000718129557) | Rupert Carlyon / 11:32–12:04 | 节目依据 |
| wealth / 突然收到一笔钱，先给自己留决定空间 | [2026-03-08 · 1000753843137](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000753843137) | Nick Crawford / 11:21–11:42 | 节目依据 |
| wealth / 看到 ethical 或 ESG，继续查它具体怎样投资 | [2026-03-01 · 1000752252957](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000752252957) | Martin Hawes / 03:00–04:50 | 节目依据 |
| wealth / 账户各自持有，不等于分开时一定各归各 | [2026-02-01 · 1000747532423](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000747532423) | Sharon Chandra / 12:31–13:03 | 节目依据 |
| wealth / 免费试用也记进账单日历，取消后留凭据 | [2025-08-10 · 1000721355600](https://podcasts.apple.com/nz/podcast/id1445636358?i=1000721355600) | Simon Brown / 32:52–33:05 | 节目依据 |

## 还没有完成的事

没有逐集通读或听音复核全部 717 份字幕；没有完成独立临床、法律或财务专业审阅。节目标题可能错位，feed 日期可能回填，自动字幕也可能误认词语与说话人。

主引用时间范围是说话人段落边界，不能当作中文摘要逐词与原音精确对齐。新出现的临床建议只保留寻求评估或沟通的动作，不把节目个案转成个体治疗方案。

完整字幕、私有台账和 SQLite 只留本地，不进入公开工程。公开发行只含自行撰写的指南、节目定位、公开目录及程序；发布状态见 README 和版本记录。
