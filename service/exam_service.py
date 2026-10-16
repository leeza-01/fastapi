from models.exam_model import Exam
from repository.exam_repository import *

def create_exam(db, exam):

    new_exam =Exam(
        exam_name=exam.exam_name,
        exam_type=exam.exam_type,
        total_marks=exam.total_marks,
        exam_date=exam.exam_date
    )

    return save_exam(db, new_exam)


def fetch_all_exams(db):
    return get_all_exams(db)

def fetch_exam_by_id(db):
    return get_exam_by_id(db, exam_)

def modify_exam(db, exam_id, exam):

    existing_exam = get_exam_by_id(db, exam_id)

    if not existing_exam:
        return {"message": "Exam not found"}

    existing_exam.exam_name = exam.exam_name
    existing_exam.exam_type = exam.exam_type
    existing_exam.total_marks = exam.total_marks
    existing_exam.exam_date = exam.exam_date

    update_exam(db)

    return existing_exam


def remove_exam(db, exam_id):

    exam = get_exam_by_id(db, exam_id)

    if not exam:
        return {"message": "Exam not found"}

    delete_exam(db, exam)

    return {"message": "Exam deleted successfully"}