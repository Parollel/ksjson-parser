#!/bin/bash
IFS=$'\n'

declare format="$(mktemp)"

ls json > json.list
for file in $(cat json.list); do 
    jq . "json/${file}" > "${format}"
    cp "${format}" "json/${file}"
    printf "已格式化 %s。\n" "${file}" 1>&2
done

mkdir -p raw/character raw/path raw/real.character raw/text raw/select.path raw/select
