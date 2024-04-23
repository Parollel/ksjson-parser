#!/bin/python

import json
import os
import sys
import time

scr_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(scr_dir)

json_file_list = []
with open('./jsonlist.txt', 'rt') as f:
    json_file_list = f.read().splitlines(False)
if not os.path.exists('./last_write_time.txt'):
    modified_list = json_file_list
else:
    modified_list = filter(lambda i: os.path.getmtime('./extract/text/' + i) > os.path.getmtime('./last_write_time.txt'), json_file_list)

new_write = False
for filename in modified_list:
    origin_json = {}
    user_text = []
    user_select = []

    with open('./json/' + filename, 'rt') as f:
        origin_json = json.load(f)
    with open('./extract/text/' + filename, 'rt') as f:
        user_text_json = json.load(f)
    with open('./extract/select/' + filename, 'rt') as f:
        user_select_json = json.load(f)

    for ujson_index, ujson_val in enumerate(user_text_json):
        if ujson_val != None:
            olist = origin_json['scenes'][ujson_index]['texts']
            for ulist_index, ulist_val in enumerate(ujson_val):
                if ulist_index % 2 == 0:
                    ulist_index //= 2
                    if isinstance(olist[ulist_index][1], list):
                        olist[ulist_index][1][0][0] = ulist_val
                    else:
                        olist[ulist_index][1] = ulist_val
                else:
                    ulist_index //= 2
                    if isinstance(olist[ulist_index][1], list):
                        olist[ulist_index][1][0][1] = ulist_val
                    else:
                        olist[ulist_index][2] = ulist_val
    for ujson_index, ujson_val in enumerate(user_select_json):
        if ujson_val != None:
            origin_json['scenes'][ujson_index]['selects'] = ujson_val

    with open('./json/' + filename, 'wt') as f:
        json.dump(origin_json, f, ensure_ascii = False, indent = None)
        print(filename + ' write DONE!', file = sys.stderr)
        new_write = True

if not new_write:
    print('No file updated, have a good day!', file = sys.stderr)
else:
    with open('./last_write_time.txt', 'wt') as f:
        f.write(time.asctime())
        print('Write time updated.', file = sys.stderr)
