from fastapi import FastAPI
from database.connection import Base, engine

from models.student_model import Student
from routers.student_router import router
from models.course_model import Course
from routers.course_routers import router as course_router



Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
app.include_router(course_router)

@app.get("/")
def home():
    return{"message":"Education managemnet sysytem"}