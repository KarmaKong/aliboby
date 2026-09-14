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

两个都提交**同一个 sitemap**：`https://chinairantrucks.com/sitemap.xml`（91 条 URL，三语全覆盖）。

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
| 提交当天 | sitemap 状态 = "成功 / Success"，已发现 91 个 URL |
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
- EN: `China–Iran TIR road freight — Wuqia to Tehran Customs in 21–23 days`
- ZH: `中国到伊朗 TIR 卡航干线 · 自乌恰口岸起算 21–23 天到德黑兰海关`
- FA: `ترانزیت تیر چین به ایران — از مرز ووچیا ۲۱ تا ۲۳ روز تا گمرک تهران`

### 短简介（~160 字符，用于黄页 meta / 目录卡片）
- EN: `First-hand cross-border TIR road-freight carrier from China consolidation hubs (Yiwu, Shenzhen, Guangzhou) to Tehran West Customs via the Wuqia and Khorgos lines. Currently 21–23 days from the Wuqia crossing, CPT/DAP, weekly departures. Lithium batteries, OOG machinery, FCL/LCL.`
- ZH: `一手中伊跨境 TIR 卡航庄家。义乌 / 深圳 / 广州集货，走乌恰线或霍尔果斯线，自乌恰口岸起算 21–23 天到德黑兰西关海关。CPT/DAP，每周二五发车。承运锂电、超限大件、整车 / 拼箱。`
- FA: `حمل‌کنندهٔ دست‌اول ترانزیت تیر از انبارهای چین (ایوو، شنژن، گوانگژو) به گمرک غرب تهران از خطوط ووچیا و خورگوس. از مرز ووچیا ۲۱ تا ۲۳ روز، CPT/DAP، حرکت هفتگی. باتری لیتیومی، بار فوق‌سنگین، کانتینری و خرده‌بار.`

### 长简介（~600 字符，用于 LinkedIn About / Crunchbase / Kompass 详情）
- EN:
```
chinairantrucks operates scheduled cross-border TIR road-freight convoys connecting industrial
consolidation hubs in China — Yiwu (Suxi), Shenzhen (Pinghu), Guangzhou (Baiyun), Shanghai — directly
to the bonded customs yards of Tehran: Tehran West Customs (Gomrok Gharb), Shahriyar Customs and
Aprin Dry Port.

Trailers are sealed at the exit gateway under a TIR carnet, which keeps unsealings and transloads to a
minimum — a direct truck is transloaded once, at Bukhara — before entering Iran at Sarakhs. Transit is
currently 21–23 days from the Wuqia crossing to the bonded warehouse (plus a domestic leg within about
7 days), on CPT / DAP terms — the consignee's licensed broker clears
the cargo in Iran's ASYCUDA system against the warehouse entry receipt (Ghabz-e Anbar).

Core services: general FTL and LCL cargo (from 1 CBM / 100 kg), Class 9 lithium batteries
(UN 3480 / 3481), solar and BESS equipment, out-of-gauge machinery on step-frame low-beds, and
chemical materials with a valid MSDS. Fleet of 45+ owned and contracted 480–540 HP curtainsider tractor-trailers, Beidou-3 + GPS telematics, electronic door seals, and CMR transit insurance up to
USD 250,000 per trailer. Registered TIR international road-transport operator with dispatch teams
stationed at the exit gateway and in Tehran. On the Central Asia legs the tractor and driver may be a
vetted partner carrier registered in the transit country.

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
| Tagline | `China–Iran TIR road freight — Wuqia to Tehran Customs in 21–23 days` |
| Logo | `brand/lockup.png`（正方形版另裁，300×300 起） |

### 3.2 About（粘贴 EN 长简介，第 1 节）

### 3.3 前 8 篇帖子（2 周，每周 3 篇，周二 / 周四 / 周六）

> 每篇配 1 张真实照片。句子短，不用感叹号堆砌。结尾统一 CTA + 3 个 hashtag。

**Post 1 — 定位**
```
We run one thing: sealed TIR trailers from China to Tehran Customs.

Consolidation at Yiwu, Shenzhen and Guangzhou → out through the Wuqia or Khorgos line under a TIR
carnet → across Central Asia with one transload at Bukhara → into the bonded warehouse at
Tehran West Customs, currently 21–23 days from the Wuqia crossing.

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
The route, leg by leg (the two legs are quoted separately, never added):
- Domestic: origin consolidation → the exit gateway, typically within about 7 days
- Exit gateway: China export clearance, TIR seal + electronic lock — the transit count starts here
- Wuqia line: Kyrgyzstan (0.4% transit tax), then Uzbekistan; a direct truck is transloaded once, at Bukhara
- Turkmenistan (Farap–Mary), then entry at Sarakhs: ASYCUDA record, bonded transit permit
- Tehran West Customs bonded warehouse, Ghabz-e Anbar issued — currently 21–23 days from the Wuqia crossing (direct truck)

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
Road (TIR): currently 21–23 days from the Wuqia crossing to the Tehran customs bonded warehouse, one transload at Bukhara.
Sea (Bandar Abbas): 35–55 days to the container yard, then a separate inland leg.

For batteries, chemicals and out-of-gauge, road is usually the only workable mode.
#OceanFreight #RoadFreight #Iran
```

**Post 6 — 口岸实拍**（配霍尔果斯照片）
```
Khorgos. Where the trailer is sealed under the carnet — which means fewer unsealings on the way, not none.
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
The transit figure is to the Tehran customs bonded warehouse — not your door, not DDP.
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

## 3b. Telegram 频道（波斯语，面向伊朗——优先级仅次于 GSC/Bing）

> 目标不同于 LinkedIn。LinkedIn 喂的是 Bing/Copilot 的**英文**实体图谱；Telegram 频道喂的是**伊朗买家的实际发现路径**，同时是一个能被搜索引擎收录的波斯语阵地。

### 3b.0 先修：当前频道简介在发作废口径 ⚠️

`t.me/Aliboby88` 已经是一个**频道**（不是个人号），但只有 2 个订阅者，且简介正在公开发布**已废止的旧 canon**：

```
حمل جاده‌ای مستقیم چین→ایران زیر پلمپ TIR. ... گمرک غرب تهران، ۱۴–۱۸ روز، CPT/DAP. ...
```

两个问题：`۱۴–۱۸ روز` 是 `AGENTS.md` §3 明确标为 stale 的数字；`مستقیم ... زیر پلمپ` 的连用贴近 §3.2 禁止的"全程封签 / 无换装"框架。这个频道被首页询价条和 Organization JSON-LD 的 `sameAs` 直接引用，**伊朗买家点过去第一眼看到的就是它**。站内口径修得再干净，这里不改等于白做。

**替换文本**（Telegram 频道简介上限 255 字符，以下约 200）：

```
حمل جاده‌ای چین→ایران زیر پلمپ TIR. ایوو/شنژن/گوانگژو تا گمرک غرب تهران و مشهد. از مرز ووچیا فعلاً ۲۱ تا ۲۳ روز تا تهران، یک تعویض بار در بخارا. CPT/DAP. کانتینری و خرده‌بار از ۱ متر مکعب. 🌐 chinairantrucks.com
```

这一步**只能你在 Telegram 里改**，我改不了。

### 3b.1 为什么 Telegram 值得投

三个已核实的事实：

| 事实 | 依据 |
|---|---|
| `t.me/s/<频道>` 是**服务端渲染**的可爬页面 | 实测抓取公开频道返回 146KB HTML、20 条消息正文可读 |
| `t.me` **没有 robots.txt**（返回 404），未声明爬取限制 | 实测 |
| Telegram 在伊朗渗透率约 **59%**，是当地**首要的企业沟通渠道** | 2026 行业统计；官方被过滤但普遍经 VPN 使用 |

配合手册的"万物皆可排名"：一个持续更新的波斯语频道本身就是可排名文档，而不只是联系方式。

> **发链接时用 `t.me/s/Aliboby88` 这个预览地址**（对外引用、给爬虫），`t.me/Aliboby88` 留给真人点击加入。

### 3b.2 与 WhatsApp 的关系——一个需要你决策的数据点

站点现在的设定（`AGENTS.md` §2）是 WhatsApp 全站主 CTA、Telegram 只在三个首页的询价条做次级按钮。但在伊朗，**Telegram 渗透率（约 59%）高于 WhatsApp（约 41%）**，两者都被过滤、都靠 VPN。

这不构成"立刻改 CTA"的结论——B2B 进口商和清关行的习惯可能与大众分布不同，而且 WhatsApp 在国际贸易场景更通用。但**只针对波斯文页面**提升 Telegram 的权重，是值得单独评估的一件事。**需要你拍板**，不要我自行改动。

### 3b.3 频道运营：8 条波斯语开篇帖

> 每条配一张真实照片。短句，不用感叹号。所有数字严格走 §3 canon——**不要写 ۱۴–۱۸、不要写 بدون تخلیه（无换装）、不要写 تضمین（保证）**。

**۱ — 定位**
```
ما یک کار می‌کنیم: تریلر پلمپ‌شده زیر کارنه تیر، از چین تا انبار گمرک تهران.

تجمیع در ایوو، شنژن و گوانگژو ← خروج از خط ووچیا یا خورگوس ← عبور از آسیای میانه با یک تعویض بار در بخارا ← ورود از سرخس ← انبار گمرک غرب تهران.

انبار به گمرک، نه درب به درب. ترخیص با حق‌العمل‌کار رسمی شماست.

chinairantrucks.com
```

**۲ — عدد واقعی**
```
از مرز ووچیا، کامیون مستقیم در حال حاضر ۲۱ تا ۲۳ روز تا تهران و ۱۸ تا ۲۱ روز تا مشهد.
کامیون با تعویض بار: ۲۶ تا ۳۰ و ۲۴ تا ۲۸ روز.

مسیر داخلی چین تا ووچیا جداگانه است — معمولاً ظرف ۷ روز. این دو را با هم جمع نمی‌کنیم.

برای خط خورگوس عددی منتشر نمی‌کنیم؛ استعلامی است.
```

**۳ — ۰٫۴٪ را کجا می‌بینید**
```
۰٫۴٪ ارزش فاکتور کالا، عوارض ترانزیت قرقیزستان است — مالیات، نه کرایه.
فقط روی خط ووچیا. خط خورگوس (از قزاقستان) هرگز آن را ندارد.

در نرخ لحاظ نشده و جداگانه صورت‌حساب می‌شود. پیش از رزرو به شما می‌گوییم بار از کدام خط می‌رود.
```

**۴ — کارنه تیر**
```
کارنه را حمل‌کننده تهیه می‌کند، نه صاحب کالا. کارنهٔ این خط سمت چین صادر می‌شود.

کارنه یعنی باز شدن پلمپ و تعویض بار کمتر — نه هیچ. کامیون مستقیم یک بار در بخارا تعویض بار می‌شود.
کارنه نه زمان حمل را تغییر می‌دهد و نه کرایه را، و معافیت از بازرسی هم نیست.
```

**۵ — خرده‌بار**
```
کنسول از ۱ متر مکعب یا ۱۰۰ کیلوگرم.
دربست: تریلر ۱۳٫۶ متری؛ برای بار فوق‌سنگین کمرشکن ۱۷٫۵ متری.
سقف هر دستگاه: ۹۶ متر مکعب و ۲۵ تن. مازاد جداگانه قیمت می‌خورد.
```

**۶ — باتری لیتیومی**
```
باتری لیتیومی کلاس ۹ (UN3480 / UN3481)، شامل BESS و LiFePO4، بار اصلی این خط است نه استثنا.
شرط: MSDS کامل ۱۶ بخشی و مدارک بسته‌بندی UN، از همان ابتدا.
```

**۷ — استعلام با سه داده**
```
برای استعلام سه چیز لازم است:
۱. انبار مبدأ — ایوو / شنژن / گوانگژو
۲. گمرک مقصد — گمرک غرب تهران / آپرین / مشهد
۳. مشخصات کالا — کد HS، وزن ناخالص (kg)، حجم (CBM)

نرخ‌ها هفتگی بازبینی می‌شوند و هر استعلام رسمی تاریخ اعتبار دارد.
```

**۸ — یک سوءتفاهم رایج**
```
عددی که می‌دهیم تا انبار گمرک است، نه تا درب شما و نه DDP.
حقوق ورودی، ترخیص و حمل داخلی بر عهدهٔ حق‌العمل‌کار رسمی صاحب کالاست.
ما قبض انبار را تحویل می‌دهیم؛ ادامهٔ کار با حق‌العمل‌کار شماست.
```

### 3b.4 节奏

- 每周 2 条，固定时间。**断更比不发更伤**——空频道比没有频道还差。
- 每条结尾放 `chinairantrucks.com` 或对应文章的深链，别加 UTM（内链不带跟踪参数，站外引用也保持干净 URL）。
- 新文章上线当天，频道同步发一条波斯语摘要 + 深链。
- 不要转发未经核实的伊朗行业新闻数字（单证涨价百分比之类）——理由见 §3.8 的同一条约束。

---

## 3c. Instagram（定位不同，优先级更低）

先把预期摆正：**Instagram 对"被搜到"这个目标几乎没有直接帮助。** Meta 对爬虫封锁很严，个人/企业主页在搜索引擎里基本拿不到有效收录，也不是 AI 的 grounding 来源。它是**转化与信任**渠道，不是 SEO/GEO 渠道——和 Telegram 是两个工种。

背景：伊朗约 4400 万人（52%）在用，官方被过滤、靠 VPN，是当地最主要的企业**展示**平台。

因此建议：

- **排在 Telegram 与 LinkedIn 之后**。目前站上没有 Instagram 账号，先不急着开。
- 真要开，定位为相册：装车、口岸、封签、到仓照片，波斯语短文案，主页链接指向 `chinairantrucks.com`。
- 照片纪律沿用 §7：不出现可读车牌、人脸、水印、敏感单据。
- 不要把它当询价入口——询价仍走 WhatsApp / Telegram / 邮箱。

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
