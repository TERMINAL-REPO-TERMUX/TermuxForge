#!/data/data/com.termux/files/usr/bin/bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PKG="$ROOT/package/forge-hello"
OUT="$ROOT/dist"
mkdir -p "$OUT"
chmod 755 "$PKG/data/data/com.termux/files/usr/bin/forge-hello"
dpkg-deb --build "$PKG" "$OUT/forge-hello_0.1.0_all.deb"
printf '\nBuilt package: %s\n' "$OUT/forge-hello_0.1.0_all.deb"
printf 'This is only the .deb build step; APT index, signing, and hosting come next.\n'
