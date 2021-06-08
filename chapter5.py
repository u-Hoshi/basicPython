# 関数を定義する
def trip(dist,speed):
  time=dist/speed
  return time

work=trip(1000,20)
bike=trip(1000,50)
print(work+bike)

# ドキュメンテーション文字列
def trip2(dist,speed):
  """距離と速度から所要時間を計算して返します
  引数:
  dist -- 距離
  speed -- 速度
  """
  time2 = dist / speed
  return time2

# pydoc
# help(trip2)

# 再帰呼び出し
  # ある関数の中から、その関数自信を呼び出すこと

def sum(n):
    if n>0:
        return n+sum(n-1)
    return 0

print(sum(10))

# 位置引数
def lunch(main,side,drink):
    print("main",main)
    print("side",side)
    print("drink",drink)

lunch("beef","bread","tea")

# キーワード引数
lunch (side="side",drink="tea",main="beef")

# 引数のデフォルト値
def dinner(main="フィッシュ",drink="コーヒー",side="ice"):
    print("main",main)
    print("drink",drink)
    print("side",side)

dinner("肉肉肉")
dinner(side="山盛りポテト")

# ラムダ式
  # 無名関数...元々関数型言語の機能だった
list=list(map(lambda x:x*x,[1,2,3,4,5]))
print(list)

# 変数のスコープ
  # global文
def cat():
    global pet
    pet ="cat"

pet="dog"
cat()
print(pet)

  # nonlocal文
def dog():
    def cat():
        # nonlocal pet
        pet="cat"
        print(pet)
    pet="dog"
    cat()
    print(pet)
dog()