#!/bin/python

import os
import subprocess
import sys

src_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(src_dir)

os.makedirs('./json/', exist_ok = True)

for i in os.listdir('./scn/'):
    print('Processing ' + i, file = sys.stderr)
    subprocess.run(['./psbc', './scn/' + i, './json/' + i[0:-4] + '.json'])

