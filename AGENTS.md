# AGENTS.md — chinairantrucks.com

Operating manual for anyone (human or AI) editing this site. Read before changing anything.

---

## 1. What this is

Static marketing site for a **China → Iran overland TIR trucking (freight-forwarding) linehaul** service — first-hand carrier running sealed trailers from Chinese consolidation hubs to Tehran West Customs, hub-to-customs (not door-to-door).
Trilingual. Audience: Iranian importers and their customs brokers (Persian, the buyer side) and Chinese exporters / factories / forwarders (Chinese). English is the third track, mainly so global AI assistants (ChatGPT / Claude / Gemini) can cite the brand.

- **Stack:** hand-written static HTML + one CSS file. No framework, no build step, no JS app. `.nojekyll` is present so files starting with `_` are served.
- **Host:** GitHub Pages, "deploy from branch", source = `main` / root. `CNAME` = `chinairantrucks.com` (apex, no `www` — `www` 301s to apex).
- **Analytics:** GoatCounter (`js/count.js`), plus an inline CTA-click event script on every page (tags clicks `wa` / `tg` / `email`).
- **Contact everywhere:** WhatsApp `https://wa.me/8613237401856` (+86 132 3740 1856) is the primary channel — it's the nav "contact" link (`class="wa contact"`) and the gold CTA button site-wide. `sales@chinairantrucks.com` is the secondary ghost button everywhere. Telegram `https://t.me/Aliboby88` is kept only as a secondary ghost button in the **quote strip of the 3 homepages** and in the Organization `sameAs`. (There is also `brand/telegram-qr.png` for `t.me/uarmside` — an offline asset, **not** linked from any page. Do not swap site Telegram links to it.)
- **Organization JSON-LD** (homepages) carries `telephone` `+8613237401856`, a WhatsApp `sameAs`, and a phone `contactPoint`.

---

## 2. URL architecture (do not restructure)

| Language | Home | Article index | Article |
|---|---|---|---|
| Persian (default, RTL) | `/` (`index.html`) | `/articles/` | `/articles/<slug>/` |
| Chinese (LTR) | `/zh.html` | `/zh/articles/` | `/zh/articles/<slug>/` |
| English (LTR) | `/en/` | `/en/articles/` | `/en/articles/<slug>/` |

- One URL = one language-locale document. No `?lang=`, no query params, no aliases.
- `<body>` class carries the language: `fa` / `zh` / `en`, plus `home` on the three homepages.
- Redirect stubs (old slugs) exist under `zh/articles/` (`first-central-asia`, `lcl-traps`, `uzbekistan-quote`) and `zh/index.html`. They use `<meta http-equiv="refresh">` + a real `<a>`. Leave them; do not add new ones — pick the final slug the first time.
- `x-default` hreflang points to the **Persian** version site-wide (matches the homepage).
- The 2026-09 copywriting guide proposed moving to `/zh/` and `/fa/` directories (Apple/Canva pattern). **Deferred** — 40+ file moves, no real 301s on GitHub Pages, ~2 weeks of lost fresh-index equity. Revisit only on an explicit decision; if done, `x-default` also moves to `/en/` per that guide.

---

## 3. The fact canon — MUST be identical across all languages and pages

Cross-page consistency of these facts is a search-ranking and AI-citation signal. Never contradict them, never "improve" the numbers, never invent new ones.

> **2026-09-07 canon revision (supersedes the earlier 2026-09 "Khorgos TIR, no transloading, 14–18 days" canon).** Operator-supplied line data replaced the previous transit and transloading claims. Any page still saying "14–18 days / 14–18 天 / ۱۴ تا ۱۸ روز", "no transloading / 免倒装 / بدون تخلیه", "22 天", or Incheboron as the Iran entry is **stale**, not canon. Reconciliation is tracked page-by-page; the three homepages are converted first.

- **Business model:** **hub-to-customs / warehouse-to-customs (仓到关 / 站到关 / انبار به گمرک).** NOT door-to-door, NOT DDP, NOT by sea. Trade terms **CPT / DAP**; the consignee's licensed broker pays duty and releases the cargo. This company does **not** do Iran customs clearance.
- **Origin consolidation hubs:** Yiwu 义乌（苏溪）· Shenzhen 深圳（平湖）· Guangzhou 广州（白云）· Shanghai 上海. Cargo can also be handed over at a supervised zone (CY / CFS) at the exit gateway.

### 3.1 The two live corridors

| | **Wuqia 乌恰 line** | **Khorgos 霍尔果斯 line** |
|---|---|---|
| Exit gateway | Wuqia 乌恰 / ووچیا | Khorgos 霍尔果斯 / خورگوس |
| Transit countries | Kyrgyzstan → Uzbekistan → Turkmenistan | Kazakhstan → Uzbekistan → Turkmenistan |
| Published routing string | `Xinjiang – Kyrgyzstan (0.4% TAX on cargo invoice) – Uzbekistan – Turkmenistan – Iran – TEHRAN` | `Xinjiang – Kazakhstan – Uzbekistan – Turkmenistan – Iran – TEHRAN` |
| Kyrgyz 0.4% transit tax | **Applies** | **Never applies** |
| Transit time | published, see 3.3 | **quote on request — no day count may be published** |

**Turgart 吐尔尕特 and Alashankou 阿拉山口 are not operated.** Say so plainly if asked; do not present them as options.

### 3.2 Transloading structure — say it exactly this way

- **Direct truck 直达车 / کامیون مستقیم:** Wuqia → **Bukhara (one transload)** → Iran.
- **Transshipment truck 换装车:** Wuqia → **Osh (transload)** → **Bukhara (transload)** → Iran, or a further transload at the Iranian border.

> "Direct" means **one transload at Bukhara**, not zero. Never write "no transloading", "免倒装", "بدون تخلیه", "straight through with no transloading", or "one seal end to end" anywhere on the site. The honest differentiator is **fewer transloads and a shorter, more predictable transit**, not zero transloads.

### 3.3 Transit time — **counted from the Wuqia border crossing**, not from the origin hub

Wuqia line, current ("目前 / currently / معمولاً" — never "guaranteed"):

| Destination | Direct 直达 | Transshipment 换装 |
|---|---|---|
| Sarakhs 萨拉赫斯 / Lotfabad 洛特法巴德 (Iran border customs) | 15–18 days | 21–24 days |
| Mashhad 马什哈德 | 18–21 days | 24–28 days |
| Tehran 德黑兰 | 21–23 days | 26–30 days |

- **The count starts at Wuqia.** The domestic leg (origin hub → Wuqia) is **not** included and is **not yet quantified** — quote it separately, never fold it into these numbers, and never present these as hub-to-destination figures.
- Khorgos line: **no transit-day figure exists.** Answer "quote on request".
- Every published day range must carry a hedge word: 目前 / currently / typical / معمولاً. No "guaranteed", no "保证".

### 3.4 Iran entry and destinations

- **Iran clearance gateways:** **Sarakhs 萨拉赫斯 / سرخس** or **Lotfabad 洛特法巴德 / لطف‌آباد**. (Incheboron 因切布伦 is **out of canon** — remove wherever it appears.)
- **Sellable destinations:** Sarakhs / Lotfabad border customs · Mashhad Customs 马什哈德 · Tehran 德黑兰 (Tehran West Customs / Gomrok Gharb / گمرک غرب تهران · Shahriyar · Aprin Dry Port). Iran customs system: **ASYCUDA**; a warehouse entry receipt (Ghabz-e Anbar / قبض انبار / 海关入库单) is issued to the consignee's broker.

### 3.5 Load limits

- **≤96 CBM and ≤25 T per vehicle.** Over-limit portions are not covered by the quote and are priced separately.
- Do not publish the older 85 CBM / 23 T figures, and do not split the limit by direct vs transshipment.

### 3.6 Cargo

- **General cargo only.** Cargo subject to statutory inspection (法检) without the inspection paperwork is **priced separately** — say "confirm case by case", never a number.
- Core categories: general FTL / LCL, Class 9 lithium batteries (UN3480 / UN3481, incl. BESS / LiFePO4), solar PV modules · inverters · transformers, out-of-gauge heavy machinery, chemical materials / resins **with a valid 16-section MSDS + UN packaging docs**. Complete vehicles / EVs on a project basis. Auto **parts** are core general cargo.
- **LCL:** consolidation from **1 CBM or 100 kg**.

### 3.7 Quotation — what is in and what is out

**Included:** full linehaul freight · domestic warehousing, handling and export customs clearance · overseas transit-agency fees.

**Excluded:** destination customs clearance · insurance · inspection · reinforcement/lashing · lifting/craneage · overseas extension charges (no-open-inspection handling, national registration certificates, radiation-limit issues) · **the Kyrgyz 0.4% transit tax (Wuqia line only)** · statutory-inspection paperwork · any over-limit (over-CBM / over-weight) portion.

- **The 0.4%:** a **tax, not freight** — 0.4% of cargo-invoice value — **only on the Wuqia (Kyrgyzstan) line.** The Khorgos–Kazakhstan corridor never adds it. Footnote-level detail, never a headline.
- **Pricing:** **no published rates.** Always "quote on request" / 运价单询 / کرایه استعلام. Rates are **revalidated weekly**; every formal quotation carries a validity date and an `RFQ-<date>-<seq>` reference.
- **To get a quote, three things:** origin hub; destination (Sarakhs/Lotfabad · Mashhad · Tehran); cargo data (HS code · gross weight KG · volume CBM).

### 3.8 Operator assertions (unchanged, not derived from line data)

- **Fleet (operator-asserted, 2026-09):** 45+ owned and contracted 480–540 HP curtainsider tractor-trailers (13.6 m tilt) to IRU transit spec, plus 17.5 m step-frame low-beds for OOG. On the Central Asia legs the tractor and driver may be a vetted **partner carrier registered in the transit country**. Do not name truck makes/brands and do not inflate the count. Do not claim "no subcontracting" or "100% own fleet".
- **Telematics:** Beidou-3 + GPS dual-mode, hourly position logs; door e-lock (electronic seal) open/close status.
- **Licensing / presence:** TIR international road-transport operator; own dispatch coordination at the exit gateway and in Tehran.
- **TIR — correct framing:** customs seal at origin plus one carnet, which means **fewer** unsealings and transloads across the transit countries — **not none** (see 3.2). TIR does **not** change the transit time and does **not** change the freight rate. Never claim TIR means no inspection or no opening.
- **Insurance:** CMR transit insurance, liability cover up to USD 250,000 per trailer load.
- **Departures:** weekly, Tuesday & Friday, from the Yiwu and Shenzhen (Pinghu) facilities.
- **CKU railway (中吉乌铁路):** under construction, **not open**. Iran cargo is still road. Do not present it as a timeline or use it to argue price.
- This site does **not** quote sea or rail.

### 3.9 Open items — do not invent values for these

- Domestic leg (origin hub → Wuqia) day count.
- Khorgos line transit times and transloading structure.
- Whether the 96 CBM / 25 T limit differs by direct vs transshipment.

If new operational data arrives (real transit days per city, rate bands, border-wait ranges), it is added only with a clear source/date and applied to **all three languages at once**.


## 4. House style

- Terse, declarative, factual. Short sentences. No marketing fluff, no clickbait, no "震惊体".
- Headings name real entities (`Wuqia vs Khorgos: the 0.4%`), not vague ones (`How to choose`).
- No "I think / obviously". State facts; label estimates as estimates.
- Persian digits (`۲۱ تا ۲۳ روز`, `۹۶ متر مکعب`, `۰٫۴٪`) for the recurring site numbers in `fa`; Western digits for quoted statistics.
- CJK place-name pairs are kept as brand (`霍尔果斯 Khorgos`, `萨拉赫斯 Sarakhs`, `德黑兰西关 Gomrok Gharb`) in all languages.
- The **operator's first-hand voice** beats AI draft prose. AI is draft labor, not the published voice. A real About page with a named person is still TODO (see `/docs` / project notes).

---

## 5. Adding or editing an article — checklist

Duplicate the language's `_post.html` template:
`articles/_post.html` · `zh/articles/_post.html` · (for English, copy an existing `en/articles/*/index.html`).

Every article page MUST have, in `<head>`:

1. `<title>` — descriptive, entity-rich, ends with ` | chinairantrucks`.
2. `<meta name="description">` — one sentence, the core facts.
3. `<link rel="canonical">` — the page's own absolute URL.
4. **hreflang set** — self + every other language that exists for this slug + `x-default` → the Persian URL. Must be **symmetric**: if you add `en`, also add `hreflang="en"` to the `fa` and `zh` versions, and add a visible `EN` nav link there.
5. Open Graph: `og:type=article`, `og:title`, `og:description`, `og:url`, `og:site_name`, `og:locale` (+ `og:locale:alternate` for each other language), `og:image` = `https://chinairantrucks.com/og.png` (+ width 1200 / height 630), `article:published_time` / `article:modified_time`.
6. Twitter card: `summary_large_image` + title/description/image.
7. **JSON-LD** — an `Article` block and a `BreadcrumbList` block (Home → Articles → this page). Every JSON-LD block must be valid JSON.

In `<body>`:

8. Standard header/nav for that language, `<main class="post"><div class="wrap">`.
9. `<p class="post-kicker">CODE</p>`, `<h1>`, optional `<time datetime>`.
10. A **Key facts** list right after the intro paragraph: `<ul class="post-facts" aria-label="要点 | خلاصه | Key facts">` with 3–4 self-contained, quotable facts drawn from this article.
11. `<figure class="hero-photo">` with a real photo from `img/` (see §7), `width`/`height` set, `loading="lazy" decoding="async"`, and a `<figcaption>`.
12. `<p class="post-links">相关： | بیشتر: | Related: ...</p>` with 2–3 internal links.
13. CTA `hero-actions` (email + Telegram) and `<p class="post-back">`.
14. The GoatCounter `<script>` + the inline CTA-tracking `<script>` (copy verbatim from any current article) + the `<noscript>` pixel with `?p=/<this path>/`.

Then:

15. Add a `way-row` to the matching article index (`articles/index.html` / `zh/articles/index.html` / `en/articles/index.html`).
16. Add the URL(s) to `sitemap.xml` (see §6).
17. If the article has genuine Q&A, add `FAQPage` JSON-LD; the `quote` pages carry `HowTo`.
18. Update `llms.txt` — the per-language article lists are generated from `<title>` tags of non-stub pages.

---

## 6. sitemap.xml

Flat `<urlset>`, regenerated whenever pages are added/removed. Priorities:

- `/` = 1.0 · `/zh.html` and `/en/` = 0.9
- the three `articles/` indexes = 0.8
- pillar articles = 0.7: `tir`, `wuqia-khorgos`, `22-days`, `quote`, `freight-cost`, `transit-time`, `ftl-vs-ltl`, `xinjiang-ports`
- everything else = 0.6

`lastmod` = the release date. Redirect stubs, `_post.html`, `404.html`, and the `google…​.html` verification file are **not** in the sitemap.

---

## 7. Assets

- `img/` — real operation photos. In use: `yard-dsab-loading.jpg` (1600×1067), `ftl-crates-rear-tm-plate.jpg` (1600×931), `tractor.jpg` / `warehouse.jpg` / `crate-marks.jpg` / `forklift.jpg` (1600×1000), `ftl-bagged-cargo.jpg` (1600×552), `pallets-strapped.jpg` (1279×1406). Compress to ~q80 progressive JPEG, strip EXIF, **no readable licence plates, no faces, no watermarks, no sensitive documents** — blur or crop first.
- `trucks/hero-cutout.png` — the tractor-unit cut-out on the homepage diagonal (generic silhouette, no brand). Design element; do not replace with a rectangular photo without CSS work.
- `brand/lockup.png` — the wordmark logo (raster). `brand/mark.png` — the circular mark, source for favicons. `og.png` — the default 1200×630 share card.
- `favicon.ico` / `favicon-32.png` / `favicon.svg` / `apple-touch-180.png` — all derived from `brand/mark.png`. Keep them in sync if the mark changes.
- Fonts self-hosted in `fonts/` (IBM Plex Sans, Outfit). CDN loads are not used.

---

## 8. CSS

- `css/tokens.css` — colour + layout variables. `css/site.css` — everything else (imports tokens).
- Palette: `--navy #0B1F3A` (dominant ink), `--gold / --brass #C4A35A` (accent — used only for "iran", numerals, CTAs, section stubs), `--paper / --cream #F5F2EB` (substrate).
- Language body fonts: `body.fa` Tahoma stack, `body.zh` PingFang stack, `body.en` IBM Plex Sans stack.
- Homepages: `body:has(.hero-cut)` makes the header a transparent overlay; `body.<lang> .home-hero` sets the paper/navy diagonal (fa mirrors the direction of zh/en). Article pages: `body:has(main.post)` gives the header the paper background.
- Reusable article components: `.post-facts`, `.post-links`, `.post-kicker`, `.hero-photo`, `.way-row`.

---

## 9. Deploy flow

1. Branch → change → open a PR against `main`. Commit messages in Chinese, describing what and why.
2. Squash-merge. GitHub Pages redeploys from `main` in ~1–2 min.
3. `.github/workflows/indexnow.yml` fires on push to `main` with HTML changes: it diffs changed pages and submits their URLs to `api.indexnow.org` (→ Bing, Yandex, Seznam, Naver). Google does **not** use IndexNow.
4. Verify live: check `gh api repos/KarmaKong/aliboby/pages/builds/latest` is `built` with no error, then curl the changed URLs for `200`.

Do not push directly to `main`. Do not force-push shared branches.

---

## 10. Do NOT

- Change any number in the fact canon (§3), or add transit-day / rate figures without a sourced first-hand basis.
- Break hreflang symmetry (every language version of a slug must list all the others + `x-default`).
- Add tracking params to internal links, or use JS redirects instead of real links.
- Auto-redirect by IP or force a language switch.
- Replace the homepage tractor cut-out, or restyle the header/diagonal, without a deliberate design pass.
- Swap the site's Telegram links (`Aliboby88`) or the `#org` JSON-LD `@id` (`https://chinairantrucks.com/#org`).
- Mass-produce near-duplicate articles that only re-slice the same facts by keyword — new pages need real information gain.
- Modify `js/count.js` (GoatCounter's own file), `CNAME`, `.nojekyll`, the IndexNow key file, or `google869b982389a5864a.html`.

---

## 11. Off-repo, human-owned

These are done in external consoles, not in the codebase:

- **Google Search Console** — sitemap + URL inspection. Covers Google, AI Overviews, Gemini.
- **Bing Webmaster Tools** — sitemap + URL submission. Covers ChatGPT, Copilot.
- **Baidu** — intentionally skipped (no ICP filing, foreign host, GitHub Pages is slow from mainland). Chinese off-site reach goes via Xiaohongshu / 公众号 / 知乎 instead.
- **Brave** — no console; it crawls the open web. `robots.txt` already allows it; the static HTML is fully readable.
