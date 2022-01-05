from typing import Optional
from pydantic import BaseModel
from decouple import config

CSRF_KEY = config("CSRF_KEY")


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


# ここでリクエストのデータ型を定義する

# リクエストした際に返ってくるデータ型
class Todo(BaseModel):
    id: str
    title: str
    description: str


# リクエストする際に使用するデータ型
class TodoBody(BaseModel):
    title: str
    description: str


class SuccessMsg(BaseModel):
    message: str


# フロントエンドから送られてくるデータ型
class UserBody(BaseModel):
    email: str
    password: str


# RESTapiのレスポンスの型
class UserInfo(BaseModel):
    id: Optional[str] = None
    email: str
