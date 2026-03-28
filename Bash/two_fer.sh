#!/usr/bin/env bash

main() {
    if [ ! -z "$1" ]; then
        local name=$1
        echo "One for $name, one for me."
    elif [ -z "$1" ]; then
        echo "One for you, one for me."
    fi
}

main "$@"
