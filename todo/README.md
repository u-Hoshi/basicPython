### 立ち上げコマンド

`python3 run.py`

### テストユーザー

ユーザ名：admin

パスワード：fastapi

### ページ構成について

```md
/ ：トップページ
/login ：ログインページ
/register ：サインアップ(ユーザ登録)ページ
```

`http://127.0.0.1:8000/doc`にアクセスすると、自動で API ドキュメントが生成される。

### DB の確認コマンド

```
$ sqlite3 db.sqlite3
.table
select * from user;
select * from task;
```

### 記事

第 1 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment

第 2 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-model-building

第 3 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-authentication-user-registration

第 4 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-admin-page-improvement

第 5 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-event-details-page-create

第 6 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-event-add-delete

第 7 回
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-web-api-complete
