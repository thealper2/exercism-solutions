#!/usr/bin/env bash

score=$1
command=$2
target_item=$3

allergens=("eggs" "peanuts" "shellfish" "strawberries" "tomatoes" "chocolate" "pollen" "cats")

my_allergies=()
for i in "${!allergens[@]}"; do
    if (( (score & (1 << i)) != 0 )); then
        my_allergies+=("${allergens[i]}")
    fi
done

if [[ "$command" == "allergic_to" ]]; then
    found="false"
    for item in "${my_allergies[@]}"; do
        if [[ "$item" == "$target_item" ]]; then
            found="true"
            break
        fi
    done
    echo "$found"

elif [[ "$command" == "list" ]]; then
    echo "${my_allergies[*]}"
fi
