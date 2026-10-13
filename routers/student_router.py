from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session


from database.connection import get_db
from schemas.student_schema import CreateStudent
from service.student_service import create_student
from service.student_service import fetchAll_Students
from service.student_service import fetchby_Id
from service.student_service import remove_student
from service.student_service import modify_student


router = APIRouter()


@router.post("/students")
def add_student(student: CreateStudent, db: Session = Depends(get_db)):
    return create_student(db, student)

@router.get("/students")
def get_students(db : Session = Depends(get_db)):
    return fetchAll_Students(db) 

@router.get("/students/{student_id}") 
def get_student(student_id:int, 
                db: Session=Depends(get_db)):
    return fetchby_Id(db, student_id)

@router.delete("/students/{student_id}")
def delete_student_data(
        student_id: int,
        db: Session = Depends(get_db)
):
    return remove_student(db, student_id)

@router.put("/students/{student_id}")
def update_student_data(
    student_id: int,
    student: CreateStudent,
    db: Session = Depends(get_db)
):
    return modify_student(
        db,
        student_id,
        student
    )