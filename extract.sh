#!/bin/bash

IFS=$'\n'

declare source="json/${1}"
declare text="raw/text/text.${1}"
declare real_character="raw/real.character/real_character.${1}"
declare display_character="raw/character/character.${1}"
declare path="raw/path/path.${1}"

jq '[path(.scenes[].texts[]?)]' "${source}" > "${path}"
jq '[.scenes[].texts[]?[0]]' "${source}" > "${real_character}"
jq '[.scenes[].texts[]?[1][0][0]]' "${source}" > "${display_character}"
jq '[.scenes[].texts[]?[1][0][1]]' "${source}" > "${text}"

printf "已处理 %s。\n" "${1}" 1>&2
