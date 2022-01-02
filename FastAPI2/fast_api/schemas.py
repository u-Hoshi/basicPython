from pydantic import BaseModel

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
