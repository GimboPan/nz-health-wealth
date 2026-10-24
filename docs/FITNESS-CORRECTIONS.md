# Fitness旧文重点校正记录

2026-10-25 · v1.2.0。四篇原网址与Fitness入口保留。这里只记录本次确认的错误、过时或过宽说法；不是对全部旧文的临床审阅或节目听音复核。

## 手写页面的校正

| 原文 | 本次重点 |
| --- | --- |
| [九章就医指南](https://gimbo.co.nz/fitness/health-hub) | 肠癌按地区起筛、乳腺按生日与地区扩龄；Shingrix资助及两剂安排；ACC渐进伤害、转介与Ka Ora收费；取消未经证实的全量听音表述。 |
| [Healthpoint使用说明](https://gimbo.co.nz/fitness/healthpoint) | 区分新注册、casual与当天预约；收窄ED门槛、urgent care速度、孕产免费和转介概括；历史价目与界面样本保留原日期。 |
| [一位GP的节目整理](https://gimbo.co.nz/fitness/one-gp) | 个人观点不代表所有GP；收窄全量听音表述，并应用下列逐项编辑校正。 |
| [酒精与成瘾专题](https://gimbo.co.nz/fitness/alcohol) | 家属服务按地区确认；谈话不保证成功；标准杯、饮酒阈值、停酒自测及复饮等见下表。 |

## 语料生成部分的独立校正

完整数据见[fitness-corrections.json](../content/fitness-corrections.json)。原值仅用于防止上游重生成后把校正套错位置；网站按守卫检查后应用新文本。校正标注公共来源，节目仍作背景；仅收窄历史概括的项目不新增现行规则承诺。

| 原文数据与目标 | 修订后的主题或表述 | 本次依据 |
| --- | --- | --- |
| `claims/referral/groups/1/items/2` | 2026年2月1日起，成人18岁以上的ADHD兴奋剂治疗可由具相应专科注册的GP及在执业范围内的NP启动；不是每家诊所或每位GP都提供此项服务。 | [Pharmac · ADHD prescribing changes](https://www.pharmac.govt.nz/news-and-resources/adhd/changes-for-prescribers) |
| `claims/mental-access/groups/3/items/3` | 2026年2月1日起，成人18岁以上的ADHD兴奋剂治疗可由具相应专科注册的GP及在执业范围内的NP启动；不是每家诊所或每位GP都提供此项服务。 | [Pharmac · ADHD prescribing changes](https://www.pharmac.govt.nz/news-and-resources/adhd/changes-for-prescribers) |
| `claims/referral` | 公立计划性专科通常先由医疗提供者评估转介；私立是否需要转介及怎样收费，要向接收服务确认。不同服务有不同入口。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/referral/groups/0` | 公立与私立：先问评估、转介和接收条件 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/referral/groups/0/items/0` | 专科路径先问接收条件：公立计划性照护通常经医疗提供者评估转介；私立也可能要求转介。 | [Health NZ · Planned care](https://www.healthnz.govt.nz/hospitals-services/services-support/planned-care) |
| `claims/referral/groups/0/items/2` | 考虑私人精神科前，先向保险方确认本人的保单是否承保、限额和预授权。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/referral/groups/3/items/0` | 等检查结果时，联系负责团队，确认谁接收、谁解释，以及预计何时回复。 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `claims/referral/groups/3/items/1` | 对判断仍有疑问，可以询问如何取得另一意见，并确认资料、转介和费用。 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `claims/referral/groups/3/items/2` | 节目曾讨论更年期专科资源不足；当前地区是否有公费或其他服务，要向负责团队查询。 | [Health NZ · Planned care](https://www.healthnz.govt.nz/hospitals-services/services-support/planned-care) |
| `claims/mental-access/groups/0/items/1` | 情绪支持服务可以通过电话或短信联系；不要预设一定会回拨或何时回拨。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/0/items/3` | 先问注册的诊所有没有HIP或其他基层心理支持，以及怎样预约。 | [Health NZ · No referral process](https://www.wellbeingsupport.health.nz/no-referral-process) |
| `claims/mental-access/groups/1/items/0` | 自费咨询的价格、时长及取消费用，要向具体提供者询问。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/1/items/1` | 若雇主提供EAP，先问覆盖哪些服务、可用次数、额外批准与隐私安排。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/1/items/4` | 有保险时，直接核对精神科、心理治疗或咨询的具体承保条款。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/2/items/0` | Gumboot Friday是年轻人咨询资助的一种入口；按服务方当前资格、名额和预约办法查询。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/2/items/1` | 联系Gumboot Friday列示的提供者时，先确认资格、资助次数和实际可预约时间。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/mental-access/groups/2/items/4` | 酒精与药物服务也可能支持家属；先确认所在地的接入、预约和费用。 | [Health NZ · CADS Auckland](https://www.healthnz.govt.nz/hospitals-services/hospitals/auckland/community-alcohol-drug-services)、[Health NZ · Help for whānau and friends](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-and-drug-services/help-for-whanau-and-friends) |
| `claims/mental-access/groups/3/items/2` | 找心理支持时，分别核对专业头衔、训练、专业组织或法定登记，以及是否处理你的问题。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/pharmacist` | 可以向药师询问用药和本地服务。是否需要预约、是否收费，以及药师能看到哪些记录，要问具体药房；自己带齐全部用药清单。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/pharmacist/groups/0` | 节目建议向熟悉社区的药师打听本地服务；能否提供相关咨询及费用，向药房确认。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/pharmacist/groups/1` | 请药师一起核对完整用药清单 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/pharmacist/groups/1/items/0` | 长期配药的药师可以帮助核对多种药物；同时主动提供其他药房、医院及自行购买的用药。 | [Health NZ · Pharmacies](https://www.healthnz.govt.nz/hospitals-services/services-support/pharmacies) |
| `claims/pharmacist/groups/2/items/0` | 在药房需要专业意见时，明确要求与注册药师交谈。 | [Health NZ · Pharmacies](https://www.healthnz.govt.nz/hospitals-services/services-support/pharmacies) |
| `claims/acc` | ACC可评估意外受伤及符合条件的工作相关渐进伤害等；不要仅凭有没有“某一下”自行排除。由医疗提供者提交资料，ACC按条件决定。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/acc/groups/0` | 先问能否申请 不以突发外力概括所有承保 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/acc/groups/0/items/0` | ACC并非只认一次突发外力：符合条件的工作相关渐进伤害、疾病或感染也可能承保。 | [ACC · Cover decisions](https://www.acc.co.nz/im-injured/how-we-manage-your-claim/cover-decisions) |
| `claims/afterhours` | 按病情紧迫程度选择入口：严重或紧急情况及时寻求急诊帮助；拿不准可问Healthline，普通问题也可联系诊所护士讨论当天选择。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/afterhours/groups/0` | 诊所护士、Healthline等可帮助判断下一步；不要把先打自己诊所写成每一种情况都必须经过的步骤。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/afterhours/groups/2` | 情绪支持、基层心理服务与急诊用途不同；存在紧急危险时及时求助，不用旧个案等待时间推断是否值得就医。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `claims/afterhours/groups/2/items/2` | 节目曾转述精神危机就医等待的个案投诉；它不能用来判断当前危机是否应求助。 | [Health NZ · Emergency departments](https://www.healthnz.govt.nz/hospitals-services/services-support/emergency-departments) |
| `claims/afterhours/groups/2/items/3` | 年轻人的咨询资助服务可作为一种选项，资格、名额和预约要向当前提供者确认。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `gp/0/items/3` | 检查结果要追踪，但GP不一定能看到所有机构的结果 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `gp/0/items/6` | 喉咙痛用药先核对适用年龄 不沿用旧节目固定阿司匹林服法 | [Healthify／Health NZ · Sore throat in children](https://healthify.nz/health-a-z/s/sore-throat-children)、[Medsafe · Use of aspirin in children（2015）](https://www.medsafe.govt.nz/profs/PUArticles/December2015/UseOfAspirinInChildren.htm) |
| `gp/1/items/0` | 保健品标签不等于疗效认证 但宣传也有监管限制 | [Medsafe · Supplying products which are not approved medicines](https://www.medsafe.govt.nz/compliance/Marketing.asp) |
| `gp/1/items/1` | 筛查要分项目 不能说70岁就一律停止 | [Health NZ · National Bowel Screening Programme](https://www.healthnz.govt.nz/about-us/what-we-do/programmes-and-initiatives/national-bowel-screening-programme)、[Health NZ · Breast screening age extension](https://www.healthnz.govt.nz/health-topics/keeping-healthy/cancer-screening/breast-screening/breast-screening-information-for-women-aged-70-and-over) |
| `gp/2/items/0` | Shingrix资助不仅看65岁 也要核对免疫条件与第二剂安排 | [Health NZ · Shingles vaccine](https://www.healthnz.govt.nz/health-topics/immunisations/vaccines-aotearoa/shingles-vaccine) |
| `gp/2/items/1` | 筛查收益不能变成个人命运 资格回到当前项目 | [Health NZ · National Bowel Screening Programme](https://www.healthnz.govt.nz/about-us/what-we-do/programmes-and-initiatives/national-bowel-screening-programme) |
| `gp/2/items/2` | 流感疫苗每年核对资助 不沿用旧族群年龄概括 | [Health NZ · Influenza immunisation handbook](https://www.healthnz.govt.nz/health-professionals/guidance-standards/topic/immunisation/immunisation-handbook/influenza) |
| `gp/2/items/3` | 标准杯是10g纯酒精 低风险建议不等于安全保证 | [Health NZ · Standard drinks（2024）](https://resources.alcohol.org.nz/assets/Uploads/8.0-AL-437-Guide-to-Standard-Drinks-May-2024.pdf)、[Health NZ · Alcohol and you（2025）](https://resources.alcohol.org.nz/assets/Uploads/6.1-AL002_Facts_effects_Brochure_Apr-2025.pdf)、[Health NZ · Alcohol addiction](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-addiction) |
| `gp/2/items/7` | 前列腺检查要分筛查与症状 不能把单一年龄写成所有人的停止线 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `gp/2/items/9` | 家庭药箱先核对成分、适用年龄与剂量 不把广播数字当处方 | [Healthify／Health NZ · Sore throat in children](https://healthify.nz/health-a-z/s/sore-throat-children)、[Health NZ · Pharmacies](https://www.healthnz.govt.nz/hospitals-services/services-support/pharmacies) |
| `gp/4/items/1` | 主动说明症状变化并追踪结果 不以“去闹”争取排队优先 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/)、[Health NZ · Planned care](https://www.healthnz.govt.nz/hospitals-services/services-support/planned-care) |
| `gp/4/items/2` | 预约前准备问题 检查是否需要提前做由团队判断 | [Health NZ · General practices](https://www.healthnz.govt.nz/hospitals-services/services-support/general-practices)、[HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `gp/4/items/6` | 按时间线描述症状 把查到的信息作为问题带去 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `gp/4/items/7` | 共同决策包括疫苗 医生强烈建议不取消同意权 | [HDC · Information, choice and consent](https://www.hdc.org.nz/your-rights/the-code-and-your-rights/your-rights-when-using-a-health-or-disability-service-what-to-do-if-you-have-any-concerns/) |
| `mental/0` | 新西兰一个标准杯含10g纯酒精，容量还取决于酒精度。读瓶身标识并如实记录；低风险建议不是人人适用的安全线，依赖者减量或停酒先寻求专业支持。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `mental/0/items/0` | 一个标准杯含10g纯酒精 容量必须结合酒精度 | [Health NZ · Standard drinks（2024）](https://resources.alcohol.org.nz/assets/Uploads/8.0-AL-437-Guide-to-Standard-Drinks-May-2024.pdf) |
| `mental/0/items/1` | 如实记录饮酒 不把所有人的自报量一律乘二 | [Health NZ · Standard drinks（2024）](https://resources.alcohol.org.nz/assets/Uploads/8.0-AL-437-Guide-to-Standard-Drinks-May-2024.pdf) |
| `mental/0/items/2` | 低风险饮酒建议要看完整条件 不能只用每周12–15杯 | [Health NZ · Alcohol and you（2025）](https://resources.alcohol.org.nz/assets/Uploads/6.1-AL002_Facts_effects_Brochure_Apr-2025.pdf) |
| `mental/0/items/6` | 量、控制感和生活影响都值得讨论 不是靠一个念头诊断 | [Health NZ · Alcohol addiction](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-addiction) |
| `mental/0/items/7` | 一周或一个月不喝不能诊断有没有问题 先考虑戒断风险 | [Health NZ · Alcohol addiction](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-addiction) |
| `mental/3` | 家属可以先为自己寻求支持。联系具体服务确认入口；选择能安全交谈的时候说明观察和担心，依赖或戒断问题交给医疗团队评估。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `mental/3/items/0` | 家属可以独立寻求支持 先确认本地入口 | [Health NZ · Help for whānau and friends](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-and-drug-services/help-for-whanau-and-friends)、[Health NZ · CADS Auckland](https://www.healthnz.govt.nz/hospitals-services/hospitals/auckland/community-alcohol-drug-services)、[Alcohol Drug Helpline · 服务方说明](https://alcoholdrughelp.org.nz/) |
| `mental/3/items/3` | 开口时说观察和担心 不把一句话当成成败开关 | [Health NZ · Help for whānau and friends](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-and-drug-services/help-for-whanau-and-friends) |
| `mental/3/items/4` | 担心身体依赖时 不自行安排突然停酒 | [Health NZ · Alcohol addiction](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-addiction) |
| `mental/3/items/8` | 复饮可能发生 可以预先约定支持计划 | [Health NZ · Alcohol addiction](https://www.healthnz.govt.nz/health-topics/mental-health/alcohol-and-drug-addiction/alcohol-addiction) |
| `claims/public-private/groups/1/items/2` | 筛查与有症状后的检查不同；公费年龄也要按具体项目、生日和地区核对。 | [Health NZ · Breast screening age extension](https://www.healthnz.govt.nz/health-topics/keeping-healthy/cancer-screening/breast-screening/breast-screening-information-for-women-aged-70-and-over)、[Health NZ · National Bowel Screening Programme](https://www.healthnz.govt.nz/about-us/what-we-do/programmes-and-initiatives/national-bowel-screening-programme) |
| `claims/public-private/groups/1/items/3` | 当前Shingrix已有资助：核对65岁第一剂及特定免疫条件，而非沿用旧产品的自费／公费对比。 | [Health NZ · Shingles vaccine](https://www.healthnz.govt.nz/health-topics/immunisations/vaccines-aotearoa/shingles-vaccine) |
| `claims/public-private/groups/2/items/2` | 等待期间症状改变，及时联系医疗团队重新评估。 | [Health NZ · Planned care](https://www.healthnz.govt.nz/hospitals-services/services-support/planned-care) |
| `mental/0/items/3` | 新西兰可以查询社区酒精与药物支持；能否预约、是否转介、费用和家属支持按本地服务确认。依赖者减量或停酒先寻求专业评估，不从泛化的walk-in说法安排当天就诊。 | 收窄旧概括／标明历史情境，不作新规则承诺 |
| `gp/2/items/5` | 孩子的牙科登记要单独确认 尚未登记也应继续询问安排 | 收窄旧概括／标明历史情境，不作新规则承诺 |

## 三块内容进入Health的方式

- [Healthpoint操作工具](guides/healthpoint-find-care.md)：新增官方补充条目，接入现有注册与口译条目。
- [问诊与结果追踪模板](guides/gp-visit-follow-up.md)：扩展现有waiting条目，并从连续照护与AI准备条目进入，不另增泛讲GP的重复条目。
- [家属饮酒问题求助](guides/alcohol-family-support.md)：新增官方补充条目，全国咨询与奥克兰服务分别说明。

没有新增或编造节目时间戳。109条节目引用、84集、104个主片段及原音频核验边界保持原样。
