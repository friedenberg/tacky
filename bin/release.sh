#! /bin/bash -e

git diff --exit-code -s || (echo "unstaged changes, refusing to release" && exit 1)

${EDITOR:-${VISUAL:-vi}} ./VERSION
git add ./VERSION
git diff --exit-code -s ./VERSION || (echo "version wasn't changed" && exit 1)
git commit -m "bumped version to $(cat ./VERSION)"
git push origin main

version="v$(cat ./VERSION)"

git diff --exit-code -s || (echo "unstaged changes, refusing to release" && exit 1)
git tag "$version" -m "$version"

