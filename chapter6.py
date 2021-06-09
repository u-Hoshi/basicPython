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

