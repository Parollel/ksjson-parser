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
declare select_path="raw/select.path/select_path.${1}"
declare select="raw/select/select.${1}"
declare output="$(mktemp)"

if [[ "$(jq -s '
    .[3] = (.[2] | length) |
    .[4][0] = ((.[0] | length) == .[3]) |
    .[4][1] = ((.[1] | length) == .[3]) |
    .[4] |
    all' "${character}" "${text}" "${path}")" == "false" ]]; then
    printf "处理 %s 时错误: 路径数与人物名或文本数不匹配。\n" "${1}" 1>&2
    exit 1
fi
if [[ -f "${select_path}" ]]; then
    if [[ "$(jq -s '(.[0] | length) == (.[1] | length)' "${select_path}" "${select}")" == "false" ]]; then
        printf "处理 %s 时错误: 分支路径数与分支数不匹配。\n" "${1}" 1>&2
        exit 2
    fi
    jq -s '
        .[6] = 0 |
        .[7] = (.[1] | length) |
        until(.[6] >= .[7];
            setpath([0] + .[1][.[6]] + [1, 0, 0]; .[2][.[6]]) |
            setpath([0] + .[1][.[6]] + [1, 0, 1]; .[3][.[6]]) |
            .[6] += 1) |
        .[8] = 0 |
        .[9] = (.[4] | length) |
        until(.[8] >= .[9];
            .[10] = getpath([0] + .[4][.[8]]) |
            .[11] = (if ((.[5][.[8]] | type) == "number")
            then .[5][.[8] - .[5][.[8]]]
            else .[5][.[8]]
            end)|
            .[12] = 0 |
            .[13] = (.[10] | length) |
            until(.[12] >= .[13];
                .[10][.[12]].text = .[11][.[12]] |
                .[12] += 1) |
            setpath([0] + .[4][.[8]]; .[10]) |
            .[8] += 1) |
        .[0]
    ' "${source}" "${path}" "${character}" "${text}" "${select_path}" "${select}" > "${output}"
else
    jq -s '
        .[4] = 0 |
        .[5] = (.[1] | length) |
        until(.[4] >= .[5];
            setpath([0] + .[1][.[4]] + [1, 0, 0]; .[2][.[4]]) |
            setpath([0] + .[1][.[4]] + [1, 0, 1]; .[3][.[4]]) |
            .[4] += 1) |
        .[0]
    ' "${source}" "${path}" "${character}" "${text}" > "${output}"
fi

cp "${output}" "${source}"
printf "已处理 %s。\n" "${1}" 1>&2
