#!/bin/bash
IFS=$'\n'

xargs -a json.list -n1 bash extract.sh

cd raw
find select/ -size '3c' | xargs rm
find select.path/ -size '3c' | xargs rm
