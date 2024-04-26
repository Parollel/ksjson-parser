#!/bin/python

import glob
import json
import os

scr_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(scr_dir)
os.chdir('./json/')

jsondir = './'

with open('../jsonlist.txt', 'wt', encoding = 'utf-8') as jsonlist:
    for f in glob.glob('*.ks.json'):
        with open(jsondir + f, 'rt', encoding = 'utf-8') as jsonfile:
            j = json.load(jsonfile)
        with open(jsondir + f, 'wt', encoding = 'utf-8') as jsonfile:
            json.dump(j, jsonfile, ensure_ascii = False, indent = None)
        jsonlist.write(f + '\n')

dir_list = [
    '../extract/text/',
    '../extract/select/'
]
for dir in dir_list:
    os.makedirs(dir, exist_ok = True)
