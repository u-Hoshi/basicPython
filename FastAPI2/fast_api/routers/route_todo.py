from fastapi import APIRouter
from schemas import Todo, TodoBody
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from database import db_create_todo
from starlette.status import HTTP_201_CREATED

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
