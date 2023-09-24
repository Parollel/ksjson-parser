#!/bin/bash
IFS=$'\n'

for file in $(cat json.list); do
    bash extract.sh "${file}"
done

cd raw
find select/ -size '3c' | xargs rm
find select.path/ -size '3c' | xargs rm
