from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session


from database.connection import get_db
from schemas.student_schema import CreateStudent
from service.student_service import create_student

router = APIRouter()


@router.post("/students")
def add_student(student: CreateStudent, db: Session = Depends(get_db)):
    return create_student(db, student)