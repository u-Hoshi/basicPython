from fastapi import FastAPI, Request
from routers import route_todo, route_auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas import SuccessMsg, CsrfSettings
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError

app = FastAPI()
app.include_router(route_todo.router)
app.include_router(route_auth.router)
# RESTAPIへアクセスできるホワイトリスト
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.1.8:3000",
    "http://localhost:3000/todo",
]
# appに対してcorsの設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "Welcome to Fast API"}
