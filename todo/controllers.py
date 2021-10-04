from fastapi import security
from starlette import requests
import db
from models import User, Task
from fastapi import FastAPI,Depends,HTTPException

from fastapi.security import HTTPBasic,HTTPBasicCredentials

from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

import hashlib

def register(request:Request):
  if request.method=="GET":
    pass
  
  if requests.method=="POST":
    pass
  
  if request.method is 'GET':
        return templates.TemplateResponse('register.html',
                                          {'request': request,
                                           'username': '',
                                           'error': []})



app = FastAPI(
  title="FastAPIで作るtodoアプリ",
  description="FastAPIの学習用チュートリアル",
  version="0.9"
)

# テンプレート関連の設定
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

security = HTTPBasic() 

def index(request:Request):
  return templates.TemplateResponse("index.html",{"request":request,})

def admin(request:Request,credentials:HTTPBasicCredentials=Depends(security)):
  username=credentials.username
  password=hashlib.md5(credentials.password.encode()).hexdigest()

  user = db.session.query(User).filter(User.username==username).first()
  task = db.session.query(Task).filter(Task.user_id==user.id).all() if user is not None else []
  db.session.close()

  if user is None or user.password != password:
    error = "ユーザ名かパスワードが間違っています"
    raise HTTPException(
      status_code=HTTP_401_UNAUTHORIZED,
      detail=error,
      headers={"WWW-Authenticate":"Basic"}
    )

  return templates.TemplateResponse("admin.html",
                                    {"request":request,
                                    "user":user,
                                    "task":task})