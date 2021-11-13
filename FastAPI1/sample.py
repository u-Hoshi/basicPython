import requests
import json

def main():
  url="https://b9qazj.deta.dev/"
  data={
    "x":1.2,
    "y":3.4
  }
  res=requests.post(url,json.dumps(data))
  print(res.json())

if __name__=="__main__":
  main()