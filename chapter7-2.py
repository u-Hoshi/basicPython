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