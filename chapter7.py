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

