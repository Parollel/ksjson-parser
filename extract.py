#!/bin/python

import json
import os
import sys
import time

src_dir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(src_dir)


def format(elem):
    def format_inner(elem):
        i, val = elem
        val = json.dumps(val, ensure_ascii = False)
        return val if i % 2 == 0 else '  ' + val

    if elem == None:
        return '\n  null'
    else:
        return '\n  [\n    ' + ',\n    '.join(list(map(format_inner, enumerate(elem)))) + '\n  ]'



json_file_list = []
with open('./jsonlist.txt', 'rt') as f:
    json_file_list = f.read().splitlines(False)

modified_list = None
if not os.path.exists('./last_extract_time.txt'):
    modified_list = json_file_list
else:
    modified_list = filter(lambda i: os.path.getmtime('./json/' + i) > os.path.getmtime('./last_extract_time.txt'), json_file_list)

new_extract = False
for filename in modified_list:
    origin_json = {}
    user_text = []
    user_select = []

    with open('./json/' + filename, 'rt') as f:
        origin_json = json.load(f)

    for ojson_index, ojson_val in enumerate(origin_json['scenes']):
        if 'texts' in ojson_val:
            while len(user_text) <= ojson_index:
                user_text.append(None)
            user_text[ojson_index] = []
            for otext in ojson_val['texts']:
                character = otext[1][0][0] if otext[1][0][0] != None else otext[0]
                user_text[ojson_index].append(character)
                user_text[ojson_index].append(otext[1][0][1])
        if 'selects' in ojson_val:
            while len(user_select) <= ojson_index:
                user_select.append(None)
            user_select[ojson_index] = ojson_val['selects']

    format_str = '[' + ','.join(list(map(format, user_text))) + '\n]'
    with open('./extract/text/' + filename, 'wt') as f:
        f.write(format_str)
    with open('./extract/select/' + filename, 'wt') as f:
        json.dump(user_select, f, ensure_ascii = False, indent = 2)
    print(filename + ' extract DONE!', file = sys.stderr)
    new_extract = True

if not new_extract:
    print('No file updated, have a good day!', file = sys.stderr)
else:
    with open('./last_extract_time.txt', 'wt') as f:
        f.write(time.asctime())
        print('Extract time updated.', file = sys.stderr)
