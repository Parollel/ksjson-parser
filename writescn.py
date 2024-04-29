#!/bin/python

import os
import subprocess
import sys

src_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(src_dir)
os.chdir('./json/')

jsondir = './'
outdir = '../out/'

os.makedirs(outdir, exist_ok = True)

with open('../jsonlist.txt', 'rt', encoding = 'utf-8') as f:
    json_file_list = f.read().splitlines(False)

for i in json_file_list:
    subprocess.run(['../FreeMoteToolkit/PsBuild.exe', '-nr', i])
    os.rename(i[0:-4] + 'psb', outdir + i[0:-4] + 'scn')
