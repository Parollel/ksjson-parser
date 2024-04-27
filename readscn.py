#!/bin/python

import glob
import os
import subprocess

src_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(src_dir)
os.chdir('./scn/')

jsondir = '../json/'
os.makedirs(jsondir, exist_ok = True)

for f in glob.iglob('*.scn'):
    subprocess.run(['../FreeMoteToolkit/PsbDecompile.exe', f])
    for s in ['json', 'resx.json']:
        dest = jsondir + f[0:-3] + s
        if os.path.exists(dest):
            os.remove(dest)
        os.rename(f[0:-3] + s, dest)
