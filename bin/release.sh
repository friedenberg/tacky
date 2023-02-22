#! /bin/bash -e

git diff --exit-code -s || (echo "unstaged changes, refusing to release" && exit 1)

file_version="./src/version.py"

${EDITOR:-${VISUAL:-vi}} "$file_version"
git add "$file_version"
git diff --exit-code -s "$file_version" || (echo "version wasn't changed" && exit 1)
git commit -m "bumped version to $(cat "$file_version")"
git push origin main

version="$("$file_version")"

git diff --exit-code -s || (echo "unstaged changes, refusing to release" && exit 1)
git tag "$version" -m "$version"

