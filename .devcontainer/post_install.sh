#!/bin/bash

set -xo pipefail

get_latest_tag() {
    git ls-remote --refs --sort="version:refname" --tags "$1" | cut -d/ -f3- | grep -v beta | tail -n1
}

# go lang
curl -sSL https://go.dev/dl/go1.18.3.linux-amd64.tar.gz | sudo tar xzf - -C /usr/local
echo "export PATH=\$PATH:/usr/local/go/bin" >>~/.zshrc

# CUE
LATEST_TAG=$(get_latest_tag https://github.com/cue-lang/cue.git)
curl -sfL https://github.com/cue-lang/cue/releases/download/"${LATEST_TAG}"/cue_"${LATEST_TAG}"_linux_amd64.tar.gz | sudo tar xzf - -C /usr/local/bin

# dagger
LATEST_TAG=$(get_latest_tag https://github.com/dagger/dagger.git)
curl -sfL https://github.com/dagger/dagger/releases/download/"${LATEST_TAG}"/dagger_"${LATEST_TAG}"_linux_amd64.tar.gz | sudo tar xzf - -C /usr/local/bin

# pip
pip install -r "$(pwd)"/requirements.txt
