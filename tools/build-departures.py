#!/usr/bin/env python3
"""Regenerate the departure-log entry block on the three language log pages.

    python3 tools/build-departures.py            # rewrite pages, print Telegram text
    python3 tools/build-departures.py --check    # validate only, touch nothing

Reads data/departures.tsv. Every published sentence is generated from enum
fields, so the person maintaining the log fills in structured data and never
writes prose — which is what keeps the log from drifting out of the AGENTS.md
§3 canon the way the off-site copy did.

It only rewrites the region between the DEPARTURES:BEGIN / DEPARTURES:END
markers on each page. Everything else on those pages is hand-written HTML and
is left byte-identical, per the §12 verification pattern.

This is an authoring aid, run by hand; its output is committed. The site still
has no build step (§1).
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "departures.tsv"

PAGES = {
    "fa": ROOT / "articles" / "departures" / "index.html",
    "zh": ROOT / "zh" / "articles" / "departures" / "index.html",
    "en": ROOT / "en" / "articles" / "departures" / "index.html",
}

# --- canon-bound vocabulary -------------------------------------------------
# Only these destinations may be published (§3.4). Sarakhs and Lotfabad are
# entry/transit gateways and internal facts respectively, never sellable
# destinations, so they deliberately have no entry here.
DEST = {
    "tehran":  {"fa": "گمرک غرب تهران", "zh": "德黑兰西关海关", "en": "Tehran West Customs"},
    "mashhad": {"fa": "گمرک مشهد",      "zh": "马什哈德海关",   "en": "Mashhad Customs"},
}
HUB = {
    "yiwu":      {"fa": "ایوو",      "zh": "义乌",   "en": "Yiwu"},
    "shenzhen":  {"fa": "شنژن",      "zh": "深圳",   "en": "Shenzhen"},
    "guangzhou": {"fa": "گوانگژو",   "zh": "广州",   "en": "Guangzhou"},
    "shanghai":  {"fa": "شانگهای",   "zh": "上海",   "en": "Shanghai"},
}
LINE = {
    "wuqia":   {"fa": "خط ووچیا",     "zh": "乌恰线",     "en": "Wuqia line"},
    "khorgos": {"fa": "خط خورگوس",    "zh": "霍尔果斯线", "en": "Khorgos line"},
}
CARGO = {
    "machinery":          {"fa": "ماشین‌آلات",          "zh": "机械设备",   "en": "machinery"},
    "electronics":        {"fa": "لوازم الکترونیکی",    "zh": "电子产品",   "en": "electronics"},
    "auto-parts":         {"fa": "قطعات خودرو",         "zh": "汽车配件",   "en": "auto parts"},
    "building-materials": {"fa": "مصالح ساختمانی",      "zh": "建材",       "en": "building materials"},
    "solar":              {"fa": "تجهیزات خورشیدی",     "zh": "光伏设备",   "en": "solar equipment"},
    "lithium":            {"fa": "باتری لیتیومی",        "zh": "锂电池",     "en": "lithium batteries"},
    "chemicals":          {"fa": "مواد شیمیایی",         "zh": "化工材料",   "en": "chemical materials"},
    "vehicles":           {"fa": "خودرو",                "zh": "整车",       "en": "complete vehicles"},
    "general":            {"fa": "کالای عمومی",          "zh": "普货",       "en": "general cargo"},
}
MODE = {
    "direct":    {"fa": "کامیون مستقیم (یک تعویض بار در بخارا)",
                  "zh": "直达车（布哈拉一次换装）",
                  "en": "direct truck (one transload at Bukhara)"},
    "transship": {"fa": "کامیون تعویض بار (اوش و بخارا)",
                  "zh": "换装车（奥什 + 布哈拉）",
                  "en": "transshipment truck (Osh and Bukhara)"},
}
STATUS = {
    "departed": {"fa": "خارج شد", "zh": "已发车", "en": "departed"},
    "arrived":  {"fa": "تحویل شد", "zh": "已到库", "en": "delivered"},
}

# Published transit ranges, counted from the Wuqia crossing (§3.3).
# The Khorgos line has no published figure at all, by design.
RANGE = {
    ("tehran", "direct"): (21, 23), ("tehran", "transship"): (26, 30),
    ("mashhad", "direct"): (18, 21), ("mashhad", "transship"): (24, 28),
}

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def fa_num(n):
    return str(n).translate(FA_DIGITS)


class Bad(Exception):
    pass


def photo_size(name):
    """Read the JPEG's real dimensions, so <img> never carries a wrong aspect
    ratio (photos in img/log/ are 1600 wide but vary between 4:3 and 16:9)."""
    data = (ROOT / "img" / "log" / name).read_bytes()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            raise Bad(f"{name} 不是合法 JPEG")
        marker, seglen = data[i + 1], int.from_bytes(data[i + 2:i + 4], "big")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h = int.from_bytes(data[i + 5:i + 7], "big")
            w = int.from_bytes(data[i + 7:i + 9], "big")
            return w, h
        i += 2 + seglen
    raise Bad(f"{name} 读不出尺寸")


def load():
    rows, force = [], False
    if not DATA.exists():
        raise Bad(f"缺少数据文件 {DATA}")
    for lineno, raw in enumerate(DATA.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith("!force"):
            force, line = True, line[: -len("!force")].strip()
        parts = [p.strip() for p in line.split("\t") if p.strip() != ""]
        if len(parts) != 9:
            raise Bad(f"第 {lineno} 行有 {len(parts)} 个字段，应为 9 个（须用 TAB 分隔）: {line!r}")
        d = dict(zip("date hub cargo line dest mode status days photo".split(), parts))
        d["_lineno"] = lineno
        validate(d, force)
        rows.append(d)
    rows.sort(key=lambda r: r["date"], reverse=True)
    return rows


def validate(d, force):
    n = d["_lineno"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d["date"]):
        raise Bad(f"第 {n} 行 date 格式应为 YYYY-MM-DD: {d['date']!r}")
    for key, table in (("hub", HUB), ("cargo", CARGO), ("line", LINE),
                       ("dest", DEST), ("mode", MODE), ("status", STATUS)):
        if d[key] not in table:
            allowed = " | ".join(table)
            extra = ""
            if key == "dest":
                extra = "（萨拉赫斯 / 洛特法巴德是内部事实，§3.4 禁止作为可售目的地发布）"
            raise Bad(f"第 {n} 行 {key}={d[key]!r} 不在允许值内：{allowed}{extra}")

    if d["photo"] != "-" and not (ROOT / "img" / "log" / d["photo"]).exists():
        raise Bad(f"第 {n} 行 photo 不存在: img/log/{d['photo']}")

    if d["status"] == "departed":
        if d["days"] != "-":
            raise Bad(f"第 {n} 行 status=departed 时 days 必须为 -")
        return

    # status == arrived
    if d["line"] == "khorgos":
        raise Bad(f"第 {n} 行：霍尔果斯线没有公开时效口径（§3.3），不得发布天数；"
                  f"请将 status 改回 departed")
    if not d["days"].isdigit():
        raise Bad(f"第 {n} 行 status=arrived 时 days 必须是数字（自乌恰口岸起算）")
    lo, hi = RANGE[(d["dest"], d["mode"])]
    days = int(d["days"])
    if not (lo <= days <= hi) and not force:
        raise Bad(
            f"第 {n} 行 days={days} 超出已公布区间 {lo}–{hi} 天（{d['dest']} / {d['mode']}）。\n"
            f"        这不一定是错的——实际单票本来就会有波动，公开区间是“目前/معمولاً”。\n"
            f"        但发布前请确认：要么改数据，要么在行尾加 !force 表示你确认要如实公布这一票。"
        )


def sentence(d, lang):
    """One log line. Assembled from the tables above — never free text."""
    hub, cargo = HUB[d["hub"]][lang], CARGO[d["cargo"]][lang]
    line, dest = LINE[d["line"]][lang], DEST[d["dest"]][lang]
    mode = MODE[d["mode"]][lang]
    if lang == "zh":
        s = f"{hub}集货，{cargo}，{line}，{mode}，发往{dest}。"
        if d["status"] == "arrived":
            s += f"自乌恰口岸起算 {d['days']} 天到库。"
        return s
    if lang == "en":
        s = f"Consolidated at {hub}. {cargo.capitalize()}, {line}, {mode}, to {dest}."
        if d["status"] == "arrived":
            s += f" {d['days']} days from the Wuqia crossing to the bonded warehouse."
        return s
    s = f"تجمیع در {hub}. {cargo}، {line}، {mode}، به {dest}."
    if d["status"] == "arrived":
        s += f" {fa_num(d['days'])} روز از مرز ووچیا تا انبار گمرکی."
    return s


def block(rows, lang):
    # fa lives at /articles/<slug>/, zh and en one level deeper at
    # /<lang>/articles/<slug>/ — so the hop back to the site root differs.
    up = "../../" if lang == "fa" else "../../../"
    out = ['<ul class="log-list">']
    for d in rows:
        date = d["date"] if lang != "fa" else fa_num(d["date"])
        badge = STATUS[d["status"]][lang]
        out.append("  <li>")
        out.append(f'    <p class="log-head"><time datetime="{d["date"]}">{date}</time>'
                   f' <span class="log-status">{badge}</span></p>')
        out.append(f"    <p>{sentence(d, lang)}</p>")
        if d["photo"] != "-":
            w, h = photo_size(d["photo"])
            out.append(f'    <figure class="log-photo"><img src="{up}img/log/{d["photo"]}"'
                       f' width="{w}" height="{h}" loading="lazy" decoding="async" alt=""></figure>')
        out.append("  </li>")
    out.append("</ul>")
    return "\n".join(out)


def telegram(rows):
    """Persian channel post for the newest entry (§3b.4: one post per departure)."""
    d = rows[0]
    lines = [
        f"🚚 {fa_num(d['date'])}",
        "",
        sentence(d, "fa"),
    ]
    if d["line"] == "wuqia":
        lo, hi = RANGE[(d["dest"], d["mode"])]
        lines.append(f"زمان معمول این مسیر: {fa_num(lo)} تا {fa_num(hi)} روز از مرز ووچیا.")
    else:
        lines.append("زمان حمل خط خورگوس اعلام نمی‌شود — استعلامی.")
    lines += ["", "🌐 chinairantrucks.com/articles/departures/"]
    return "\n".join(lines)


def main():
    check_only = "--check" in sys.argv
    try:
        rows = load()
    except Bad as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1

    if len(rows) < 3:
        print(f"✗ 只有 {len(rows)} 条记录。日志页至少需要 3 条才值得上线——"
              f"一条记录的日志页比没有日志页更伤信任。\n"
              f"  先在 data/departures.tsv 里补足，再跑一次。", file=sys.stderr)
        return 1

    for lang, path in PAGES.items():
        if not path.exists():
            print(f"✗ 缺少页面 {path.relative_to(ROOT)}", file=sys.stderr)
            return 1
        html = path.read_text(encoding="utf-8")
        pat = re.compile(r"(<!-- DEPARTURES:BEGIN -->).*?(<!-- DEPARTURES:END -->)", re.S)
        if not pat.search(html):
            print(f"✗ {path.relative_to(ROOT)} 缺少 DEPARTURES:BEGIN/END 标记", file=sys.stderr)
            return 1
        new = pat.sub(lambda m: m.group(1) + "\n" + block(rows, lang) + "\n" + m.group(2), html)
        newest = rows[0]["date"]
        new = re.sub(r'(<meta property="article:modified_time" content=")[^"]*',
                     lambda m: m.group(1) + newest, new)
        new = re.sub(r'("dateModified":")[^"]*', lambda m: m.group(1) + newest, new)
        if not check_only and new != html:
            path.write_text(new, encoding="utf-8")
        print(f"{'（仅校验）' if check_only else '已写入'} {path.relative_to(ROOT)}")

    print(f"\n{len(rows)} 条记录，最新 {rows[0]['date']}")
    print("\n--- Telegram 波斯语帖子（复制到频道）---")
    print(telegram(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
