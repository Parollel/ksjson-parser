import os
import requests
import sys

url = 'https://api.github.com/repos/Parollel/scntool/releases/latest'
durl: dict = {}
release = requests.get(url).json()
for i in release["assets"]:
    if i["name"] == "psbc-x86_64-linux":
        durl["linux"] = i["browser_download_url"]
    if i["name"] == "psbc-x86_64-win.exe":
        durl["win"] = i["browser_download_url"]

print('请输入数字选择您使用的操作系统:')
print('1:Windows')
print('2:Linux')
i = input('>>')
while (not i.isdigit()) or (not (int(i) <= 2 and int(i) > 0)):
    print('无效输入,请重新输入!', file = sys.stderr)
    i = input('>>')
s = int(i)

if s == 1:
    rf = requests.get(durl["win"])
    with open('./psbc.exe', "wb", encoding = 'utf-8') as f:
        f.write(rf.content)
else:
    rf = requests.get(durl["linux"])
    with open('./psbc', "wb", encoding = 'utf-8') as f:
        f.write(rf.content)

os.makedirs('./scn', exist_ok = True)
