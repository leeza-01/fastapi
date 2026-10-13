from models.student_model import Student
from repository.student_repository import save_student


def create_student(db, student_data):
    student = Student(
        student_name=student_data.student_name,
        email=student_data.email,
        phone=student_data.phone
    )

    return save_student(db, student)