# タプル
item = ("blue","hat")
print(item)

# パック
item2 ="red","shrit"
print(item2)

# アンパック 分割代入みたいもの、、、？
color ,name = item2
print(color)

# タプルのリスト
catalog=[("blue","hat"),("red","shirt"),("green","socks")]
print(catalog)

# タプルは決まった個数のデータに向く
# リストは個数が決まらないデータに向く

# enumerate関数
 # enumerate関数とはfor文と一緒に使う関数
for index,item in enumerate(catalog,1):
    print(index,item)

# 可変長引数とタプル
def test(*x):
    print(x)

test(1,2)
test(1,3,5)

def sum(*number):
    s=0
    for n in number:
        s +=n
    return s

print(sum(1,2,5,7))

#6-2 集合
  # リストやタブルに比べて制限はあるがそのぶん処理は早い
  # JSにはない概念だから新鮮
zoo ={"lion","tiger","elephant"}
print(zoo)

# メンバーシップ・テスト演算子
  # 指定した値の要素が含まれていない場合はTrue,含まれている場合はFalseを返す。
  # JSのincludesに近い
be="elephant" in zoo
print(be)

# 要素の追加
zoo |={"snake"}
print(zoo)

zoo -={"tiger"}
print(zoo)

#積集合を求める&演算子
zoo1 ={"lion","tiger","elephant"}
zoo2={"panda","snake","lion"}

print(zoo1&zoo2)

# 和集合を求める|演算子
print(zoo1|zoo2)

# 差集合を求める-演算子
print(zoo1-zoo2)

# 対称差を求める^演算子
print(zoo1^zoo2)

# 6-3 辞書
  # キーと値の組み合わせを格納できる
topping ={"bacon":210,"mushroom":140,"onion":100}
print(topping)
print(topping["onion"])

for key in topping:
    print(key)

# キーと値の取得
for key,value in topping.items():
    print(key,value)

# 要素の追加と変更
topping["bacon"]=1939
print(topping)

# 要素の削除
del topping["bacon"]
print(topping)

# 可変長引数と辞書
def test(**x):
    print(x)

test(a=4,b=5)

# 内包表記
  #データ構造を簡潔に定義する
[x**2 for x in range(1,10)]

  #内包表記を使わないバージョン
a=[]
for x in range(1,10):
    a.append(x ** 2)

  #内包表記とif
[x for x in range(1,10)if x % 3 ==0]

# 三項演算子
x=2
"fizz" if x % 3 == 0 else x

# ジェネレータ式

  # 内包表記
number =[x for x in range(1000000)]
for n in number:
    print(n)

  # ジェネレータ式
number2 = (x for in range(1000000))
for n in number:
    print(n)