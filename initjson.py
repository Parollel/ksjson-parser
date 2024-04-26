#!/bin/python

import os
scr_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(scr_dir)

with open('./jsonlist.txt', 'wt', encoding = 'utf-8') as jsonlist:
    jsonlist.writelines(map(lambda i: i + '\n', os.listdir('./json/')))
    pass

dir_list = [
    './extract/text/',
    './extract/select/'
]
for dir in dir_list:
    os.makedirs(dir, exist_ok = True)
