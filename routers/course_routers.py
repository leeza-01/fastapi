from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.course_schema import CourseCreate
from service.course_servvice import (
    create_course,
    fetch_all_courses,
    fetch_course_by_id,
    modify_course,
    remove_course
)

router = APIRouter()


@router.post("/courses")
def add_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return create_course(db, course)


@router.get("/courses")
def get_courses(
    db: Session = Depends(get_db)
):
    return fetch_all_courses(db)


@router.get("/courses/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return fetch_course_by_id(db, course_id)


@router.put("/courses/{course_id}")
def update_course_data(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return modify_course(
        db,
        course_id,
        course
    )


@router.delete("/courses/{course_id}")
def delete_course_data(
    course_id: int,
    db: Session = Depends(get_db)
):
    return remove_course(db, course_id)