import db
from models import User, Task
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
  title="FastAPIで作るtodoアプリ",
  description="FastAPIの学習用チュートリアル",
  version="0.9"
)

# テンプレート関連の設定
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


def index(request:Request):
  return templates.TemplateResponse("index.html",{"request":request,})

def admin(request:Request):
  user = db.session.query(User).filter(User.username=="admin").first()
  task = db.session.query(Task).filter(Task.user_id==user.id).all()
  db.session.close()
  return templates.TemplateResponse("admin.html",
                                    {"request":request,
                                    "user":user,
                                    "task":task})