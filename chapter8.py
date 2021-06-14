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
