from typing import List
from schemas import Todo, TodoBody, SuccessMsg
from fastapi import APIRouter, Depends, Request, Response, HTTPException
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
from fastapi_csrf_protect import CsrfProtect
from auth_utils import AuthJwtCsrf

router = APIRouter()
auth = AuthJwtCsrf()

# post(パス,返ってくるjsonのデータ型)
@router.post("/api/todo", response_model=Todo)
async def create_todo(
    request: Request,
    response: Response,
    data: TodoBody,
    csrf_protect: CsrfProtect = Depends(),
):
    new_token, _ = auth.verify_csrf_update_jwt(request, csrf_protect, request.headers)
    # auth.verify_csrf_update_jwtでエラーだった場合は以下の処理が行われない
    todo = jsonable_encoder(data)  # jsonから辞書型に変換
    res = await db_create_todo(todo)
    response.status_code = HTTP_201_CREATED
    # 新しいnew_tokenで書き換える
    response.set_cookie(
        key="access_token",
        value=f"Bearer {new_token}",
        httponly=True,
        samesite="none",
        secure=True,
    )
    if res:  # 正しく動作しデータが存在するとき
        return res
    raise HTTPException(status_code=404, detail="create task failed")


@router.get("/api/todo", response_model=List[Todo])
async def get_todo(request: Request):
    auth.verify_jwt(request)
    res = await db_get_todos()
    return res


@router.get("/api/todo/{id}", response_model=Todo)
async def get_single_todo(request: Request, response: Response, id: str):
    res = await db_get_single_todo(id)
    (new_token,) = auth.verify_update_jwt(request)
    response.set_cooke(
        key="access_token",
        value=f"Bearer {new_token}",
        httpOnly=True,
        samesite="none",
        secure=True,
    )
    if res:
        return res
    raise HTTPException(status_code=404, detail=("Task of ID]{id} doesn't exist"))


@router.put("/api/todo/{id}", response_model=Todo)
async def update_todo(
    request: Request,
    response: Response,
    id: str,
    data: TodoBody,
    csrf_protect: CsrfProtect = Depends(),
):
    new_token = auth.verify_csrf_update_jwt(request, csrf_protect, request.headers)
    todo = jsonable_encoder(data)
    res = await db_update_todo(id, todo)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {new_token}",
        httponly=True,
        samesite="none",
        secure=True,
    )
    if res:
        return res
    raise HTTPException(status_code=404, detail="update task failed")


@router.delete("/api/todo/{id}", response_model=SuccessMsg)
async def delete_todo(
    request: Request,
    response: Response,
    id: str,
    csrf_protect: CsrfProtect = Depends(),
):
    new_token = auth.verify_csrf_update_jwt(request, csrf_protect, request.headers)
    res = await db_delete_todo(id)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {new_token}",
        httponly=True,
        samesite="none",
        secure=True,
    )
    if res:
        return {"message": "Successfully deleted"}
    raise HTTPException(status_code=404, detail="delete task failed")
