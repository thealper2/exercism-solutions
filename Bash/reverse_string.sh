#!/usr/bin/env bash

main() {
    local name=$1
    echo "$name" | rev
}

main "$@"
