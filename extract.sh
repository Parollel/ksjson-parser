#!/bin/bash

IFS=$'\n'

declare source="json/${1}"
declare text="raw/text/text.${1}"
declare real_character="raw/real.character/real_character.${1}"
declare display_character="raw/character/character.${1}"
declare path="raw/path/path.${1}"
declare select_path="raw/select.path/select_path.${1}"
declare select="raw/select/select.${1}"

jq '[path(.scenes[].texts[]?)]' "${source}" > "${path}"
jq '[.scenes[].texts[]?[0]]' "${source}" > "${real_character}"
jq '[.scenes[].texts[]?[1][0][0]]' "${source}" > "${display_character}"
jq '[.scenes[].texts[]?[1][0][1]]' "${source}" > "${text}"
jq '[path(.scenes[].selects[]?)] | map(. = .[:3]) | unique' "${source}" > "${select_path}"
jq '[.scenes[].selects | select(. != null)] |
    map(reduce .[] as {$text} ([]; . += [$text])) |
    reduce .[] as $entry ([0];
        . += (if ((.[0] % 2) != 0)
            then [$entry]
            else null
            end) |
        .[0] += 1) |
    .[1:]' "${source}" > "${select}"

printf "已处理 %s。\n" "${1}" 1>&2
