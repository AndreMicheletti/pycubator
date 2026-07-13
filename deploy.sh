#!/bin/bash
set -e

# Clean and build
make clean && make build

# Get the current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Create a temporary directory for staging
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Copy docs content to temp directory
cp -r docs/* "$TEMP_DIR/"

# Stash current changes
git stash

# Switch to gh-pages branch (create if it doesn't exist)
if git rev-parse --verify gh-pages >/dev/null 2>&1; then
    git checkout gh-pages
else
    git checkout --orphan gh-pages
    git rm -rf .
fi

# Remove all files except .git
git ls-files -z | xargs -0 rm -f
rm -rf *

# Copy docs content from temp directory
cp -r "$TEMP_DIR"/* .

# Add and commit
git add .
git commit -m "Deploy: Update GitHub Pages from $CURRENT_BRANCH" || echo "Nothing to commit"
git push

# Switch back to original branch
git checkout "$CURRENT_BRANCH"
git stash pop || true

echo "Deployed to gh-pages successfully!"
