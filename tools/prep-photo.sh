#!/usr/bin/env bash
# Prepare an operation photo for publication, per AGENTS.md §7.
#
#   tools/prep-photo.sh SOURCE.jpg img/log/2026-08-31-curtainsider-loaded.jpg [WIDTH]
#
# Resizes to WIDTH (default 1600, matching the rest of img/), strips every
# metadata block including EXIF/GPS, and writes a progressive JPEG at q80.
# Prints the final dimensions so they can be pasted straight into the
# <img width= height=> attributes that §5 requires.
#
# This is an authoring aid run by hand; its output is committed. The site
# itself still has no build step (§1) — GitHub Pages serves the committed JPEG.
#
# It does NOT judge content. Licence plates, faces, customer brand names and
# readable paperwork must be cleared by eye first — see §7 and the triage
# notes in docs/growth-kit.md.
set -euo pipefail

src=${1:?usage: prep-photo.sh SOURCE DEST [WIDTH]}
dest=${2:?usage: prep-photo.sh SOURCE DEST [WIDTH]}
width=${3:-1600}

[ -f "$src" ] || { echo "源文件不存在: $src" >&2; exit 1; }
mkdir -p "$(dirname "$dest")"

magick "$src" \
  -auto-orient \
  -resize "${width}x>" \
  -strip \
  -interlace Plane \
  -sampling-factor 4:2:0 \
  -quality 80 \
  "$dest"

read -r w h < <(magick identify -format '%w %h\n' "$dest")
bytes=$(wc -c < "$dest" | tr -d ' ')
printf '%s\n' "$dest"
printf '  尺寸 %sx%s  体积 %sKB\n' "$w" "$h" "$((bytes / 1024))"
printf '  <img src="../../%s" width="%s" height="%s" loading="lazy" decoding="async" alt="">\n' "$dest" "$w" "$h"

# Fail loudly if anything survived the strip.
if magick identify -verbose "$dest" | grep -qiE 'exif:|gps:'; then
  echo "  ⚠️ 仍残留 EXIF/GPS，请检查" >&2
  exit 1
fi
printf '  EXIF/GPS 已清除 ✓\n'
