package main

import (
    "dagger.io/dagger"

    "github.com/dagger/dagger/ci/markdownlint"
    "github.com/dagger/dagger/ci/shellcheck"
)

dagger.#Plan & {
    client: filesystem: ".": read: exclude: [
        "bin"
    ]
    client: env: {
        DAGGER_LOG_FORMAT: string | *"auto"
        DAGGER_CACHE_FROM: string | *""
        DAGGER_CACHE_TO: string | *""
        GITHUB_ACTIONS: string | *""
        ACTIONS_RUNTIME_TOKEN: string | *""
        ACTIONS_CACHE_URL: string | *""
        TESTDIR: string | *"."
    }

    actions: {
        _source: client.filesystem.".".read.contents

        lint: {
            shell: shellcheck.#Lint & {
                source: _source
            }

            markdown: markdownlint.#Lint & {
                source: _source
                files: ["README.md"]
            }

            
        }
    }

}
