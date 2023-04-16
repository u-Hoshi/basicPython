from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    print("remote")
    print("debug!")
    return {"message": "hello world!"}
