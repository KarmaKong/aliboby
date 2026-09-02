# AGENTS.md — chinairantrucks.com

Operating manual for anyone (human or AI) editing this site. Read before changing anything.

---

## 1. What this is

Static marketing site for a **China → Iran overland trucking (freight forwarding)** service.
Trilingual. Audience: Iranian importers (Persian, the buyer side) and Chinese exporters (Chinese). English is the third track, mainly so global AI assistants (ChatGPT / Claude / Gemini) can cite the brand.

- **Stack:** hand-written static HTML + one CSS file. No framework, no build step, no JS app. `.nojekyll` is present so files starting with `_` are served.
- **Host:** GitHub Pages, "deploy from branch", source = `main` / root. `CNAME` = `chinairantrucks.com` (apex, no `www` — `www` 301s to apex).
- **Analytics:** GoatCounter (`js/count.js`), plus an inline CTA-click event script on every page.
- **Contact everywhere:** `exim@isacogroup.com` and Telegram `https://t.me/Aliboby88`. (There is also `brand/telegram-qr.png` for `t.me/uarmside` — an offline asset, **not** linked from any page. Do not swap site Telegram links to it.)

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

---

## 3. The fact canon — MUST be identical across all languages and pages

Cross-page consistency of these facts is a search-ranking and AI-citation signal. Never contradict them, never "improve" the numbers, never invent new ones.

- **Two corridors out of Xinjiang (新疆 / سین‌کیانگ):**
  - **Wuqia 乌恰 / Irkeshtam 伊尔克什坦 / ووچیا** — via **Kyrgyzstan**. Chain: Xinjiang — Kyrgyzstan — Uzbekistan — Turkmenistan — Iran.
  - **Khorgos 霍尔果斯 / خورگوس** — via **Kazakhstan**. Chain: Xinjiang — Kazakhstan — Uzbekistan — Turkmenistan — Iran.
- **The 0.4%:** applies **only on the Wuqia route** (crossing Kyrgyzstan). It is **0.4% of the goods' invoice value**, a **tax, not freight**, billed as a separate line item. **Khorgos does not add it.**
- **Transit time:** **about 22 days to the Tehran terminal (德黑兰场站 / پایانهٔ تهران)** — NOT door-to-door, NOT DDP, NOT by sea. **Mashhad (马什哈德) and Sarakhs (萨拉赫斯) get no day count — quote only.**
- **Destination cities:** Mashhad / Tehran / Sarakhs.
- **Cargo classes:** auto parts 汽配 · electronics 电子 · machinery 机械 · building materials 建材.
- **Services:** FTL / LTL (整车 / 零担) · terminal delivery (场站交货) · pay in RMB or offshore.
- **TIR:** customs seal at origin + one carnet; fewer openings and truck changes — "**fewer, not zero**". TIR does **not** fix the transit time or the freight.
- **Pricing:** **no published rates.** Always "quote on request" / 运费单询 / کرایه استعلام.
- **To get a quote, four things:** item name; quantity or weight; destination city; Wuqia or Khorgos. (On the Wuqia route also give the invoice value, for the 0.4%.)
- **Clearance:** buyer's, at destination. This company does **not** do Iran customs clearance.
- **CKU railway (中吉乌铁路):** under construction, **not open**. Iran cargo is still road. Do not present it as a timeline or use it to argue price.
- This site does **not** quote sea or rail.

If new operational data arrives (real transit days per city, rate bands, border-wait ranges), it is added only with a clear source/date and applied to **all three languages at once**.

---

## 4. House style

- Terse, declarative, factual. Short sentences. No marketing fluff, no clickbait, no "震惊体".
- Headings name real entities (`Wuqia vs Khorgos: the 0.4%`), not vague ones (`How to choose`).
- No "I think / obviously". State facts; label estimates as estimates.
- Persian digits (`۲۲ روز`, `۰٫۴٪`) for the recurring site numbers in `fa`; Western digits for quoted statistics.
- CJK place-name pairs are kept as brand (`乌恰 Wuqia`, `霍尔果斯 Khorgos`) in all languages.
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

- `img/` — real operation photos. In use: `yard-dsab-loading.jpg` (1600×1067), `ftl-crates-rear-tm-plate.jpg` (1600×931), `tractor.jpg` / `warehouse.jpg` / `crate-marks.jpg` / `forklift.jpg` (1600×1000). Compress to ~q80 progressive JPEG, strip EXIF, **no readable licence plates, no watermarks, no sensitive documents** — blur or crop first.
- `trucks/hero-cutout.png` — the Scania cut-out on the homepage diagonal. Design element; do not replace with a rectangular photo without CSS work.
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
- Replace the homepage Scania cut-out, or restyle the header/diagonal, without a deliberate design pass.
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
