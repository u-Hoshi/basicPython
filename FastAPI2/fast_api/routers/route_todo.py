from typing import List
from fastapi import APIRouter
from schemas import Todo, TodoBody, SuccessMsg
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from database import (
    db_create_todo,
    db_delete_todo,
    db_get_todos,
    db_get_single_todo,
    db_update_todo,
)
from starlette.status import HTTP_201_CREATED
from typing import List

router = APIRouter()

# post(パス,返ってくるjsonのデータ型)
@router.post("/api/todo", response_model=Todo)
async def create_todo(requests: Request, response: Response, data: TodoBody):
    todo = jsonable_encoder(data)  # jsonから辞書型に変換
    res = await db_create_todo(todo)
    response.status_code = HTTP_201_CREATED
    if res:  # 正しく動作しデータが存在するとき
        return res
    raise HTTPException(status_code=404, detail="create task failed")


@router.get("/api/todo", response_model=List[Todo])
async def get_todos():
    res = await db_get_todos()
    return res


@router.get("/api/todo/{id}", response_model=Todo)
async def get_single_todo(id: str):
    res = await db_get_single_todo(id)
    if res:
        return res
    raise HTTPException(status_code=404, detail=("Task of ID]{id} doesn't exist"))


@router.put("/api/todo/{id}", response_model=Todo)
async def update_todo(id: str, data: TodoBody):
    todo = jsonable_encoder(data)
    res = await db_update_todo(id, todo)
    if res:
        return res
    raise HTTPException(status_code=404, detail="update task failed")


@router.delete("/api/todo/{id}", response_model=SuccessMsg)
async def delete_todo(id: str):
    res = await db_delete_todo(id)
    if res:
        return {"message": "Successfully deleted"}
    raise HTTPException(status_code=404, detail="delete task failed")