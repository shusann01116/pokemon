#!/bin/bash

set -xo pipefail

curl -sfL https://releases.dagger.io/dagger/install.sh | sh
echo "export PATH=\$PATH:$(pwd)/bin" >>~/.zshrc
pip install -r $(pwd)/requirements.txt
