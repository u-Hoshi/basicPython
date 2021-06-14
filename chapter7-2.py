# デコレータ
import functools

def deco(f):
    @functools.wraps(f)
    def wrapper(*x,**y):
        print("begin")
        f(*x,**y)
        print("END")
    return wrapper

@deco
def hello():
    print("hello")

hello()

# 静的メソッド
  # クラスに関する情報を参照・設定の用途に向く
class Player:
   LEVEL_LIMIT=10

   @staticmethod
   def print_limit():
       print(Player.LEVEL_LIMIT)

Player.print_limit()

# クラスメソッド
  # 静的メソッド同様クラスに関する情報を参照・設定の用途に向く
class Player2:
    LEVEL_LIMIT=20

    @classmethod
    def print_limit(cls):
      print(cls.LEVEL_LIMIT)

Player2.print_limit()

class Player3:
    LEVEL_LIMIT =30

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self,value):
        if value>Player3.LEVEL_LIMIT:
            value=Player3.LEVEL_LIMIT
        self.__level = value

p=Player3()
p.level=100
print(p.level)

# インスタンス関数
class Player4:
      pass
p=Player4()
print(isinstance(p,Player4))

# 抽象クラス
  # インスタンスが作れない関数のこと

import abc

class Player5(abc.ABC):
    @abc.abstractclassmethod
    def battle(self):
          pass

class Fighter(Player5):
    def battle(self):
        print("slash")

class Wizard(Player5):
    def battle(self):
        print("magic")

# 演算子のオーバロード
  # addメソッド
class Color:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
    
    def print(self):
        print(self.r,self.g,self.b)

    
    def __add__(self,other):
        r = self.r+other.r
        g = self.g+other.g
        b = self.b+other.b
        return Color(r,g,b)

c1=Color(10,20,30)
c1.print()

c2=Color(20,430,49,)
c2.print()

c3=c1+c2
c3.print()

  # strメソッド
