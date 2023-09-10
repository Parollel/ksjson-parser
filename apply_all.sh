#!/bin/bash
IFS=$'\n'
for file in $(cat json.list); do
    bash apply.sh "${file}"
done
