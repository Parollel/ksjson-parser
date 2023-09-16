#!/bin/bash

IFS=$'\n'

cleanup() {
    [[ -f "${output}" ]] && rm "${output}"
}
trap cleanup EXIT

declare source="json/${1}"
declare path="raw/path/path.${1}"
declare character="raw/character/character.${1}"
declare text="raw/text/text.${1}"
declare output="$(mktemp)"

if [[ "$(jq -s '. += [(.[2] | length)] | .[4][0] = ((.[0] | length) == .[3]) | .[4][1] = ((.[1] | length) == .[3]) | .[4] | all' "${character}" "${text}" "${path}")" == "false" ]]; then
    printf "处理 %s 时错误: 路径数与人物名或文本数不匹配。\n" "${1}" 1>&2
    exit 1
fi

jq -s '.[4] = 0 | .[5] = (.[1] | length) | until(.[4] >= .[5]; setpath([0] + .[1][.[4]] + [1, 0, 0]; .[2][.[4]]) | setpath([0] + .[1][.[4]] + [1, 0, 1]; .[3][.[4]]) | .[4] += 1) | .[0]' "${source}" "${path}" "${character}" "${text}" > "${output}"
cp "${output}" "${source}"

printf "已处理 %s。\n" "${1}" 1>&2
