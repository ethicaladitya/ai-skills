#!/usr/bin/env bash
# Symlink every skill in this repo into a skills directory (default: ~/.claude/skills).
#   ./install.sh                      -> ~/.claude/skills
#   ./install.sh ~/.hermes/skills/x   -> any other directory
# Existing non-symlink folders with the same name are left alone (reported, not overwritten).
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$HOME/.claude/skills}"
mkdir -p "$DEST"
for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  [ -f "$dir/SKILL.md" ] || continue
  target="$DEST/$name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "skip  $name (a real folder already exists at $target)"
    continue
  fi
  ln -sfn "${dir%/}" "$target"
  echo "link  $name -> $target"
done
