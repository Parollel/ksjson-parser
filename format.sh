#!/bin/bash
IFS=$'\n'

declare format="$(mktemp)"

cleanup() {
    [[ -f "${format}" ]] && rm "${format}"
}
trap cleanup EXIT

ls json > json.list
cat json.list | while read -r file ; do
    jq . "json/${file}" > "${format}"
    cp "${format}" "json/${file}"
    printf "已格式化 %s。\n" "${file}" 1>&2
done

mkdir -p raw/character raw/path raw/real.character raw/text raw/select.path raw/select
