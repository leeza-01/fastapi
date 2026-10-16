from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.exam_schema import CreateExam

from service.exam_service import create_exam
from service.exam_service import fetch_all_exams
from service.exam_service import fetch_exam_by_id
from service.exam_service import modify_exam
from service.exam_service import remove_exam

router = APIRouter()

@router.post("/exams")
def add_exam(
    exam: CreateExam,
    db: Session= Depends(get_db)
):
    return create_exam(db, exam)


@router.get("/exams")
def get_exams(
    db: Session = Depends(get_db)
):
    return fetch_all_exams(db)

@router.get("/exams/{exam_id}")
def get_exam(
    exam_id: int,
    db: Session= Depends(get_db)
):
    return fetch_exam_by_id(
        db,
        exam_id
    )


@router.put("/exams/{exam_id}")
def update_exam_data(
    exam_id: int,
    exam: CreateExam,
    db: Session = Depends(get_db)
):
    return modify_exam(
        db,
        exam_id,
        exam
    )


@router.delete("/exams/{exam_id}")
def delete_exam_data(
    exam_id: int,
    db: Session = Depends(get_db)
):
    return remove_exam(
        db,
        exam_id
    )
