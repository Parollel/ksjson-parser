#!/bin/bash
IFS=$'\n'
for file in $(cat json.list); do
    bash extract.sh "${file}"
done
