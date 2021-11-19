from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from . import crud,models,schemas
from .database import SeesionLocal,engine
from sql_app.schemas import Booking, Room, User

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():# セッションを獲得する関数
  db=SeesionLocal()
  try:
    yield db
  finally:
    yield db.close()

@app.get("/")
# async def index():
#   return {"message":"success"}

# Read
@app.get("/users",response_model=List[schemas.User])
async def read_users(users:User):
  return {"users":users}
  
@app.get("/rooms")
async def rooms(rooms:Room):
  return {"rooms":rooms}

@app.get("/bookings")
async def bookings(bookings:Booking):
  return {"bookings":bookings}


# Create
@app.post("/users")
async def users(users:User):
  return {"users":users}
  
@app.post("/rooms")
async def rooms(rooms:Room):
  return {"rooms":rooms}

@app.post("/bookings")
async def bookings(bookings:Booking):
  return {"bookings":bookings}  