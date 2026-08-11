#!/usr/bin/env bash
# Installs gems locally (if needed) and serves the Jekyll site at http://localhost:4000
set -euo pipefail

cd "$(dirname "$0")/.."

bundle check --path vendor/bundle >/dev/null 2>&1 || bundle install --path vendor/bundle

exec bundle exec jekyll serve --watch
