from fastapi import FastAPI
from database.connection import Base, engine

from models.student_model import Student
from routers.student_router import router
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return{"message":"Education managemnet sysytem"}