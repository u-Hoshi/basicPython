# オブジェクト指向
  # クラスは設計図
  # インスタンスは設計図から生成された製品
class Player:
    def display(self):
        print("name",self.name)
        print("level",self.level)
    def display2(self):
        print("222")

p1=Player()
p1.name="hoge"
p1.level=1
p1.display()

# __init__メソッド
class Player2:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def display(self):
        print("name",self.name)
        print("level",self.level)

    # メソッドの追加
    def level_up(self,number):
      self.level+=number

p2=Player2("hoge",100)
p2.level_up(3)
p2.display()

# マングリング
  # クラスの内部だけで使うメソッドを定義

class Player3:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def display(self):
        print("name",self.name)
        print("level",self.level)

    # メソッドの追加
    def level_up(self,number):
      self.level+=number
      self.__check_level()

    # 内部のみで使えるメソッド
    def __check_level(self):
        if self.level>10:
            self.level=10
            print("10レベに達しています")

p3=Player3("player3",1)
p3.level_up(29)
p3.display()

# クラス属性と定数
class Player4:
    LEVEL_LIMIT=10

    def __init__(self,name,level):
        self.name=name
        self.level=level

    def display(self):
        print("name",self.name)
        print("level",self.level)

    # メソッドの追加
    def level_up(self,number):
      self.level+=number
      self.__check_level()

    # 内部のみで使えるメソッド
    def __check_level(self):
        if self.level>Player4.LEVEL_LIMIT:
            self.level=Player4.LEVEL_LIMIT
            print("10レベに達しています!!!")

p4=Player4("player4",1)
p4.level_up(29)
p4.display()

# 継承
  # 
  # 基底クラスにあるメソッドを派生クラスで再定義することを「オーバーライド」という。
  # 下記では__init__メソッドとdisplayメソッドをオーバーライドをしている
class Fighter(Player4):

    def __init__(self,name,level,sword):
        Player4.__init__(self,name,level)
        self.sword=sword
    
    def display(self):
          Player4.display(self)
          print("sword",self.sword)

    def sword2(self):
        print("sword!!!",self.sword2)

f=Fighter("foo",29,"black")
f.display()
f.sword2()

# 多重継承
  # 複数の基底クラスを定義
# 略

# 例外処理
number =["1","2","three","4"]
sum = 0
for n in number:
    try:
        sum+=int(n)
    except ValueError:
        print(ValueError)
print(sum)

# elseとfinally

try:
    print("try")
except ValueError:
    print("except")
else:
    print("else")
finally:
    print("finally")