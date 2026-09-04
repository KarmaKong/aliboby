# 站外增长工具包 — LinkedIn + B2B 黄页 + 实体信号

> 目的：给 `chinairantrucks.com` 在全网建立一致的"真实实体"信号，加速搜索引擎与 AI（ChatGPT/Claude/Gemini）把域名和"中伊 TIR 卡航"强关联。
> 这些**由人执行**（注册账号、填表、发帖都要在你名义下做，我不能代做）。本文备好所有可直接粘贴的材料。

---

## 0. 你必须先补的信息（缺了下面的表就填不全）

| 项 | 说明 | 状态 |
|---|---|---|
| **注册地址 / 办公地址** | 至少一个可公示的地址（公司注册地，或义乌/深圳仓库地址）。黄页和 Google Business Profile 都要。 | ⬜ 待你提供 |
| **成立年份** | 用于 LinkedIn / Crunchbase | ⬜ |
| **团队规模** | 区间即可（1-10 / 11-50…） | ⬜ |
| **营业执照 / 统一社会信用代码** | 部分黄页要，不公开也行 | ⬜ |
| **TIR 经营资质编号 / IRU 会员号** | 有就填，是强信任信号 | ⬜ |
| **一个可运营公司页的个人 LinkedIn 账号** | LinkedIn 公司页必须挂在个人号下 | ⬜ |
| **3-5 张带 EXIF 的真实照片** | 车队、装车、口岸、仓库。用于 LinkedIn 和黄页相册 | ⬜ |
| **1 票脱敏的历史运单记录** | 品名+方数+实际耗时+入库凭证（打码）。用于第一篇案例文章 | ⬜ |

---

## 0b. 搜索引擎站长工具（GSC + Bing）— 最优先，一次性

两个都提交**同一个 sitemap**：`https://chinairantrucks.com/sitemap.xml`（75 条 URL，三语全覆盖）。

### Google Search Console — https://search.google.com/search-console

1. 选 **域名属性（Domain property）**，填：
   ```
   chinairantrucks.com
   ```
   （不带 `https://`、不带 `www`、不带斜杠）
2. 验证：在域名 DNS 里加一条 **TXT 记录**（跟加 Zoho MX 记录同一个地方），值 GSC 会给。
3. 验证通过 → 左侧 **Sitemaps** → 输入 `sitemap.xml` → 提交。
4. 几天后看 **页面 / Pages** 报告和 **体验 / hreflang**（旧版"International Targeting"）有没有报错。

> 一个域名属性覆盖三语，不要建 URL 前缀属性、不要单独加 `www` / `zh.html` / `en/`。

### Bing Webmaster Tools — https://www.bing.com/webmasters

- **最省事**：做完 GSC 后用 **"Import from Google Search Console"** 一键导入（自动验证 + 带 sitemap）。
- 手动：添加站点填 `https://chinairantrucks.com`（带 `https://`，不带 www）→ 验证（XML 文件 / meta 标签 / DNS）→ **Sitemaps** 提交 `https://chinairantrucks.com/sitemap.xml`。
- URL 提交不用管：IndexNow 已接好，每次合并到 `main` 自动推送 Bing / Yandex（key 文件 `132ea0186220b34b6e12ad5428d0620433d1d80513cb2148.txt` 已验证返回 200）。

### 不用做

- ❌ `www.chinairantrucks.com`（301 跳 apex）
- ❌ 逐个提交页面 URL（sitemap 全覆盖）
- ❌ Baidu（已定放弃）
- ➕ 可选：**Yandex Webmaster**（中亚 / 俄语走廊，IndexNow 已在推），填法同 Bing

### 提交后的验证节奏

| 时间 | 看什么 |
|---|---|
| 提交当天 | sitemap 状态 = "成功 / Success"，已发现 75 个 URL |
| 3–7 天 | GSC "已编入索引的网页" 开始 > 0；Bing "已编入索引的网页" 开始 > 0 |
| 2–4 周 | GSC "效果 / Performance" 出现展示量（impressions）；开始有品牌词 + 长尾词曝光 |
| 持续 | 每周扫一眼"未编入索引"原因；hreflang / 结构化数据报告无红色错误 |

---

## 1. NAP 标准资料块（全网保持逐字一致）

> **NAP = Name / Address / Phone。** 在每一个平台粘一模一样的字段——不一致会削弱实体信号。

```
Business name:      chinairantrucks
Website:            https://chinairantrucks.com
Primary phone:      +86 132 3740 1856   (WhatsApp)
Email:              sales@chinairantrucks.com
Also on:            Telegram https://t.me/Aliboby88
Category:           International road freight forwarding / Cross-border TIR trucking
Origin countries:   China
Destination:        Iran (via Kazakhstan & Turkmenistan)
Service area:       China → Iran overland corridor (Khorgos – Kazakhstan – Turkmenistan – Sarakhs – Tehran)
Address:            << 你提供 >>
Founded:            << 你提供 >>
Company size:       << 你提供 >>
```

### 一句话简介（tagline，各语言 ≤ 60 字符）
- EN: `China–Iran TIR road freight — hub to Tehran Customs in 14–18 days`
- ZH: `中国到伊朗 TIR 卡航干线 · 14–18 天直达德黑兰海关`
- FA: `ترانزیت تیر چین به ایران — ۱۴ تا ۱۸ روز تا گمرک تهران`

### 短简介（~160 字符，用于黄页 meta / 目录卡片）
- EN: `First-hand cross-border TIR road-freight carrier from China consolidation hubs (Yiwu, Shenzhen, Guangzhou) to Tehran West Customs. 14–18 days, CPT/DAP, weekly departures. Lithium batteries, OOG machinery, FCL/LCL.`
- ZH: `一手中伊跨境 TIR 卡航庄家。义乌 / 深圳 / 广州集货，经霍尔果斯直出，14–18 天到德黑兰西关海关。CPT/DAP，每周二五发车。承运锂电、超限大件、整车 / 拼箱。`
- FA: `حمل‌کنندهٔ دست‌اول ترانزیت تیر از انبارهای چین (ایوو، شنژن، گوانگژو) به گمرک غرب تهران. ۱۴ تا ۱۸ روز، CPT/DAP، حرکت هفتگی. باتری لیتیومی، بار فوق‌سنگین، کانتینری و خرده‌بار.`

### 长简介（~600 字符，用于 LinkedIn About / Crunchbase / Kompass 详情）
- EN:
```
chinairantrucks operates scheduled cross-border TIR road-freight convoys connecting industrial
consolidation hubs in China — Yiwu (Suxi), Shenzhen (Pinghu), Guangzhou (Baiyun), Shanghai — directly
to the bonded customs yards of Tehran: Tehran West Customs (Gomrok Gharb), Shahriyar Customs and
Aprin Dry Port.

Trailers are sealed once at Khorgos under a TIR carnet and run straight through Kazakhstan and
Turkmenistan with no unsealing and no transloading, entering Iran at Sarakhs. Transit is 14–18
calendar days, hub to bonded warehouse, on CPT / DAP terms — the consignee's licensed broker clears
the cargo in Iran's ASYCUDA system against the warehouse entry receipt (Ghabz-e Anbar).

Core services: general FTL and LCL cargo (from 1 CBM / 100 kg), Class 9 lithium batteries
(UN 3480 / 3481), solar and BESS equipment, out-of-gauge machinery on step-frame low-beds, and
chemical materials with a valid MSDS. Fleet of 45+ Scania and Volvo tractors with curtainsider
trailers, Beidou-3 + GPS telematics, electronic door seals, and CMR transit insurance up to
USD 250,000 per trailer. Registered TIR international road-transport operator with dispatch teams
stationed at Khorgos and in Tehran. No subcontracting layer.

Weekly departures, Tuesday and Friday. Quote on request: sales@chinairantrucks.com /
WhatsApp +86 132 3740 1856.
```
- ZH / FA 版：把上面对应到网站首页 `.lead-brief` + 支柱页 `china-to-iran-tir-trucking` 的正文即可，保持逐字一致。

### specialties / 关键词标签（LinkedIn "Specialties"，黄页"经营范围"）
```
China Iran freight forwarding · TIR trucking · cross-border road freight · Khorgos corridor ·
Tehran West Customs · Gomrok Gharb · overland transport to Iran · lithium battery logistics ·
UN3480 UN3481 · out-of-gauge cargo · FCL LCL consolidation · Central Asia transit ·
Kazakhstan Turkmenistan transit · CPT DAP customs delivery · 中伊卡航 · 霍尔果斯口岸 ·
德黑兰海关 · 锂电池出口物流
```

---

## 2. B2B 目录 / 黄页提交清单（按"对实体识别帮助"排序）

> 原则（Loki Yan playbook）：**只提交高质量、真人会看的目录**。不要碰垃圾外链农场——对 DR 没用，还可能反噬。核心目的不是等黄页来人，是让爬虫在全网确认 `chinairantrucks.com` = 真实的中伊物流实体。

### 第一梯队（先做，实体信号最强）

| 平台 | 网址 | 需要什么 | 费用 | 备注 |
|---|---|---|---|---|
| **LinkedIn Company Page** | linkedin.com/company/setup/new | 个人号 + 邮箱 + logo + NAP | 免费 | 见第 3 节。**最高优先级**——微软生态，喂 Bing/Copilot |
| **Google Business Profile** | business.google.com | 地址 或 服务区域 + 电话验证 | 免费 | 货代可用"服务区域"模式（不显示门店地址）。地址你提供后就能做 |
| **Crunchbase** | crunchbase.com/add-new | 邮箱 + 长简介 + 成立年 | 免费版可 | AI 抓公司实体常引用 Crunchbase |
| **Kompass** | kompass.com（找"add your company"） | 公司资料 + 经营范围 + 邮箱 | 免费基础版 | 欧洲 B2B 主力目录，权重高 |
| **Europages** | europages.co.uk → "Register your company" | 公司资料 + 产品/服务分类 | 免费基础版 | 同上，欧洲采购商常用 |

### 第二梯队（物流垂直，有真实询盘可能）

| 平台 | 网址 | 备注 |
|---|---|---|
| **JCtrans 锦程物流网** | jctrans.com | 中国货代圈黄页 + 同行询盘，注册公司会员 |
| **Freightos 目录 / Shipa** | freightos.com | 全球货代目录，填服务航线 |
| **Made-in-China 供应商页** | made-in-china.com | 挂"物流服务"类目，海外买家会搜 |
| **阿里国际站公司主页** | 若已有店铺，补全"物流服务"介绍并链官网 | |
| **65logistics / 一带一路物流联盟类** | 搜"中吉乌 / 中亚 卡航 货代联盟" | 行业协会目录，权重看具体站 |

### 第三梯队（伊朗本地，转化面向清关行/进口商，门槛高）

| 平台 | 备注 |
|---|---|
| **Iran Yellow Pages** (aggah.ir، 118.ir، jesarat) | 波斯语提交，用 FA 简介。伊朗站在 Google 索引里权重一般，但对"波斯语实体"有帮助 |
| **伊朗货代 / 清关行论坛（如 tarabar.com 相关目录）** | 谨慎，选有编辑审核的 |

### 提交时的统一动作
1. 每个平台都用第 1 节的 NAP **逐字**粘贴。
2. 官网链接一律填 `https://chinairantrucks.com`（不带 UTM、不带尾斜杠变体）。
3. 简介按平台字数上限选 60 / 160 / 600 三档中的一档，**不要临时改写**。
4. 分类统一选"Freight forwarding / Road transport / Logistics"，不要选"Trucking company（本地搬运）"。
5. 相册传第 0 节的真实照片，文件名英文（`khorgos-convoy.jpg` 之类）。

---

## 3. LinkedIn 公司页工具包

### 3.1 建页字段（linkedin.com/company/setup/new）

| 字段 | 填 |
|---|---|
| Name | `chinairantrucks` |
| LinkedIn public URL | `linkedin.com/company/chinairantrucks`（若被占用，用 `chinairantrucks-logistics`） |
| Website | `https://chinairantrucks.com` |
| Industry | `Truck Transportation` 或 `Freight and Package Transportation` |
| Company size | << 你提供 >> |
| Company type | `Privately Held` |
| Tagline | `China–Iran TIR road freight — hub to Tehran Customs in 14–18 days` |
| Logo | `brand/lockup.png`（正方形版另裁，300×300 起） |

### 3.2 About（粘贴 EN 长简介，第 1 节）

### 3.3 前 8 篇帖子（2 周，每周 3 篇，周二 / 周四 / 周六）

> 每篇配 1 张真实照片。句子短，不用感叹号堆砌。结尾统一 CTA + 3 个 hashtag。

**Post 1 — 定位**
```
We run one thing: sealed TIR trailers from China to Tehran Customs.

Consolidation at Yiwu, Shenzhen and Guangzhou → out through Khorgos under a TIR carnet →
straight across Kazakhstan and Turkmenistan, no transloading → into the bonded warehouse at
Tehran West Customs in 14–18 days.

Hub-to-customs, not door-to-door. Your broker clears in ASYCUDA against the Ghabz-e Anbar.

Quote: sales@chinairantrucks.com
#ChinaIranTrade #TIRtransport #FreightForwarding
```

**Post 2 — 班期**
```
Departures this line: every Tuesday and Friday, from the Yiwu and Shenzhen (Pinghu) facilities.
LCL from 1 CBM or 100 kg. FTL on 13.6 m curtainsiders, 17.5 m low-beds for out-of-gauge.

Send origin hub + destination customs + HS code / weight / volume for a rate.
#Logistics #CrossBorderTrucking #Tehran
```

**Post 3 — 路线科普**
```
The route, stage by stage:
Day 1–2  origin consolidation
Day 3–4  Khorgos: China export clearance, TIR seal + electronic lock
Day 5–11 Kazakhstan (Almaty–Shymkent) and Turkmenistan (Farap–Mary), sealed, no unsealing
Day 12–14 Sarakhs: entry, ASYCUDA record, bonded transit permit
Day 15–18 Tehran West Customs bonded warehouse, Ghabz-e Anbar issued

#SupplyChain #TIR #CentralAsia
```

**Post 4 — 锂电能力**
```
Class 9 lithium batteries are a core service on this line, not an exception.
UN 3480 / 3481, industrial BESS, LiFePO4 packs — trailers with fire-retardant partitions to ADR.
Requirement: a full 16-section MSDS and UN packaging documents, stated up front.

#LithiumBattery #DangerousGoods #EnergyStorage
```

**Post 5 — 对比海运**
```
Road vs sea to Iran, plainly:
Road (TIR): 14–18 days to the Tehran customs bonded warehouse, sealed end to end.
Sea (Bandar Abbas): 35–55 days to the container yard, then a separate inland leg.

For batteries, chemicals and out-of-gauge, road is usually the only workable mode.
#OceanFreight #RoadFreight #Iran
```

**Post 6 — 口岸实拍**（配霍尔果斯照片）
```
Khorgos. Where the trailer is sealed once and doesn't get opened again until Tehran.
[caption the photo: date, direction, what's on the truck — no faces / plates if sensitive]
#Khorgos #BorderCrossing #Xinjiang
```

**Post 7 — 询价怎么发**
```
A quote needs three things:
1. Origin hub — Yiwu / Shenzhen / Guangzhou
2. Destination customs — Tehran West Customs / Aprin Dry Port / Mashhad
3. Cargo data — HS code, gross weight (kg), volume (CBM)

Add an MSDS for lithium/chemicals, a dimensioned drawing for out-of-gauge.
sales@chinairantrucks.com
#Freight #Quote #Importers
```

**Post 8 — 常见误区**
```
"14–18 days" is to the Tehran customs bonded warehouse — not your door, not DDP.
Import duty, clearance and local delivery are the consignee's licensed broker.
We hand over the Ghabz-e Anbar; the broker takes it from there.

#CustomsClearance #Incoterms #Iran
```

### 3.4 目标客户检索式（在 LinkedIn 搜索栏 / Sales Navigator 用）

找**伊朗进口商 / 采购**：
```
("import manager" OR "procurement" OR "sourcing" OR "purchasing manager")
AND (Iran OR Tehran OR "تهران") AND (China OR "import from China")
```
找**中国出口商 / 工厂外贸**：
```
("export manager" OR "foreign trade" OR "外贸经理") AND (Iran OR "Middle East") AND (Yiwu OR Shenzhen OR Guangzhou)
```
找**迪拜转口 / 货代同行**（转询盘来源）：
```
("freight forwarder" OR "logistics") AND (Dubai OR "Jebel Ali") AND (Iran OR "TIR")
```
每周加 15–20 个精准联系人，附一句话（不群发模板腔）：提到共同的走廊/口岸即可。

### 3.5 节奏与 hashtag 池
- 频率：每周 3 帖，持续。断更比不发更伤。
- 轮换 hashtag（每帖 3 个）：`#ChinaIranTrade #TIRtransport #FreightForwarding #CrossBorderTrucking #Logistics #SupplyChain #Khorgos #Tehran #CentralAsia #DangerousGoods #LithiumBattery #OceanFreight #Incoterms #CustomsClearance`

---

## 4. 小红书 / 微信公众号（国内向，你已在做，仅列要点）

- 选题：卡航 vs 海运成本对比、锂电池出海通道、霍尔果斯口岸实操、中亚过境单证。
- 国内大模型（DeepSeek / 豆包 / 通义）高频抓这两个平台——在中文搜索场景里，这是把 `chinairantrucks` 做成"权威信源"的最快路径。
- 每篇文末放官网链接 + 一句"完整版在官网 chinairantrucks.com"。

---

## 5. 一次性 vs 持续

| 一次性（1–2 天做完） | 持续（每周） |
|---|---|
| 建 LinkedIn 公司页 + About | LinkedIn 3 帖 |
| 提交第一、二梯队黄页（~10 个） | LinkedIn 加 15–20 精准联系人 |
| Google Business Profile | 小红书 / 公众号 1–2 篇 |
| Crunchbase | 有新发车 / 口岸照片就发 |

---

## 6. 我（Claude）能接着做的

- 把 EN 长简介同步生成 **ZH / FA 版**（与官网逐字一致）
- 写**第一篇口岸案例文章**的框架——但需要你先给第 0 节那份脱敏运单记录
- 更多 LinkedIn 帖子模板（第 9–20 篇）
- 帮你核对某个黄页提交页面该怎么填（贴截图给我）
