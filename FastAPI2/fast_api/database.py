from decouple import config
from typing import Union
from fastapi.exceptions import HTTPException
import motor.motor_asyncio
from bson import ObjectId
from auth_utils import AuthJwtCsrf

MONGO_API_KEY = config("MONGO_API_KEY")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_API_KEY)
database = client.API_DB
collection_todo = database.todo
collection_user = database.user
auth = AuthJwtCsrf()


def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": str(todo["title"]),
        "description": str(todo["description"]),
    }


def user_serializer(user) -> dict:
    return {"id": str(user["_id"]), "email": user["email"]}


# FastAPIからMongoDBに対して新しいタスクを作成する関数
async def db_create_todo(data: dict) -> Union[dict, bool]:
    todo = await collection_todo.insert_one(data)
    new_todo = await collection_todo.find_one({"_id": todo.inserted_id})
    if new_todo:
        return todo_serializer(new_todo)
    return False


# タスクを一覧取得する関数
async def db_get_todos() -> list:
    todos = []
    for todo in await collection_todo.find().to_list(length=100):
        todos.append(todo_serializer(todo))
    return todos


# 1つのタスクを取得
async def db_get_single_todo(id: str) -> Union[dict, bool]:
    todo = await collection_todo.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_serializer(todo)
    return False


# タスクを更新する関数
async def db_update_todo(id: str, data: dict) -> Union[dict, bool]:
    todo = await collection_todo.find_one({"_id": ObjectId(id)})
    if todo:
        update_todo = await collection_todo.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if update_todo.modified_count > 0:
            new_todo = await collection_todo.find_one({"_id": ObjectId(id)})
            return todo_serializer(new_todo)
    return False


# タスクを削除する関数
async def db_delete_todo(id: str) -> bool:
    todo = await collection_todo.find_one({"_id": ObjectId(id)})
    if todo:
        deleted_todo = await collection_todo.delete_one({"_id": ObjectId(id)})
        if deleted_todo.deleted_count > 0:
            return True
    return False


# ユーザーの新規作成
async def db_signup(data: dict) -> dict:
    # 引数として受けるデータはフロントエンドでユーザーが入力したpwとemailを受け取る
    email = data.get("email")
    password = data.get("password")
    overlap_user = await collection_user.find_one({"email": email})
    if overlap_user:  # emailの重複がないかを確認　既に存在したらエラーを返す
        raise HTTPException(status_code=400, detail="Email is already token")
    if not password or len(password) < 6:  # pwが入力されていないor6文字未満の場合はエラー
        raise HTTPException(status_code=400, detail="password too short")
    user = await collection_user.insert_one(
        {"email": email, "password": auth.generate_hashed_pw(password)}
    )
    new_user = await collection_user.find_one({"_id": user.inserted_id})
    return user_serializer(new_user)


# ログイン
async def db_login(data: dict) -> str:
    email = data.get("email")
    password = data.get("password")
    user = await collection_user.find_one({"email": email})
    if not user or not auth.verify_pw(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    # 問題がなかったらJWTを生成
    token = auth.encode_jwt(user["email"])
    return token
