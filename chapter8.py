# 標準ライブラリ
  # モジュール
    # 部品

import random as r
print(r.random())

print(r.randint(1,6))

# choice関数

flavor =["hoge","foo"]
print(r.choice(flavor))

# shuffle関数
card = ["1","2","3","4"]
rCard= r.shuffle(card)

import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2021,7,7)-datetime.date.today())

# 実行時間の計測
import time
old = time.time()
s=""
for i in range(1000000):
    s += "一丁目2番地"
print(time.time()-old)

old=time.time()
s="一丁目" * 1000000
print(time.time()-old)

# コマンドライン引数を受け取る

import sys
total = 0
for price in sys.argv[1:]:
    total += int(price)
print(total)

# キーボードからの入力を受け取る

total = 399
while total<=300:
    price =input()
    total+=int(price)
    print(total)

# ファイルの入出力
file = open("greeting.txt","w")
file.write("hello world")
file.close()

# JSON

import json
menu =[
  {"name":"ハンバーガー","price":100,"calorie":200},
  {"name":"チーズバーガー","price":360,"calorie":400}
]
with open("menu.txt","w") as file:
    json.dump(menu,file, indent=4)

# jsonデータからpython
with open("menu.txt","r")as file:
    menu=json.load(file)
print(menu)

# 正規表現
r"[0-9]{7}"

import re
hoge=re.match(r'[0-9]{7}',"12223442")
print(hoge)

hoge=re.fullmatch(r'[0-9]{7}',"12223442")
print(hoge)