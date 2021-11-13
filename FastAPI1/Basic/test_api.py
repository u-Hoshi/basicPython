import requests
import json

def main():
  url="http://localhost:8000/item" # エンドポイント
  body={
    "name": "hoge",
    "description": "foo",
    "price": 100,
    "tax": 1.5    
  }
  res=requests.post(url,json.dumps(body)) 
  #bodyはあくまで辞書型だから、それをjson.dumpsでjson形式に変換する
  print(res.json())


if __name__ == "__main__":
  main()