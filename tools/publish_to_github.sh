#!/usr/bin/env bash
set -euo pipefail
repo_url="https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics.git"
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Run this script from the repository root." >&2
  exit 1
fi
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$repo_url"
else
  git remote add origin "$repo_url"
fi
git push -u origin main
git push origin --tags
