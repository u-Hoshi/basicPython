print(1)

# 繰り返し処理
price = [199,199,399]
for p in price:
    print(p)

price2 = [100,120,150]
for p in price2:
    print(int(p *0.675))
    # 小数を整数にするときは"int"


# 条件分岐

temp = 18
if temp < 20 :
    print("heater")

# else
if temp < 20:
    print("heater")
else:
    print("stop")

# elif →JSでいうelse if
temp=34
if temp < 20:
    print("heater")
elif temp >=30:
    print("cooler")
else:
    print("stop")

# メンバーシップテスト演算子
  # コマンドライン上でないと帰ってこない？

"力" in "カカカカカ"

"力" not in "カカカカカ"

card = [1,3,5,6]
7 in card

# 論理演算子
temp = 18
if 15<= temp and temp <25:
    print("go outside")

if not (15 <= temp and temp <25):
    print("stay inside")

# 条件に基づく繰り返し
stage =3
while stage <=6:
  print(stage)
  stage+=1

  # break
stage =1
while stage<=8:
    print(stage)
    if stage==4:
      break
    stage +=1

  # continue
stage=1
while stage<=8:
    print(stage)
    if stage == 4:
        stage=8
        continue
    stage+=1

# range関数
for i in range(5):
    print(i)

for i in range(2,7):
    print(i)

for i in range(3,9,2):
    print(i)

# reversed関数
fruit = ["apple","banana","coconut"]
for f in reversed(fruit):
    print(f)

score = [80,90,90]

for s in score:
  if s < 70:
    break
else: #問題なく全て実行できた時のみ処理が行われる
  print("合格")

# pass文
stage = 1
while stage<=8:
    print(stage)
    if stage==4:
        pass
    stage+=1