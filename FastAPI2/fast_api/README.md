## 仮想環境に入るコマンド

`source ../env_api/bin/activate`

## 立ち上げ

`uvicorn main:app --reload`

## API ドキュメント

http://localhost:8000/docs

## mongoDB に関するドキュメント

find_one に関して

https://motor.readthedocs.io/en/stable/api-asyncio/asyncio_motor_collection.html#motor.motor_asyncio.AsyncIOMotorCollection.find_one

insert_one に関して

https://pymongo.readthedocs.io/en/3.12.0/api/pymongo/results.html#pymongo.results.InsertOneResult

## Heroku へのデプロイ方法

```
$ heroku login #CLIからherokuにアクセスしてプロジェクトを作る
$ git init
$ heroku git:remote -a hogehoge
$ git add .
$ git commit -m "コミットメッセージ"
$ git push heroku master
```

## パッケージのバージョンを txt に出力

```
$ pip freeze -> requirements.txt
```

## ファイルに関して

database.py には mongoDB と連携するための処理

schemas.py にはエンドポイントに渡すデータ型などを定義
