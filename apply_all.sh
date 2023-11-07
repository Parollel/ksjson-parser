#!/bin/bash
IFS=$'\n'

xargs -a json.list -n1 bash apply.sh
