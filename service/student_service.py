from models.student_model import Student
from repository.student_repository import save_student
from repository.student_repository import getallStudents
from repository.student_repository import getBy_Id
from repository.student_repository import delete_student
from repository.student_repository import update_student

def create_student(db, student_data):
    student = Student(
        student_name=student_data.student_name,
        email=student_data.email,
        phone=student_data.phone
    )

    return save_student(db, student)

def fetchAll_Students(db):
    return getallStudents(db)

def fetchby_Id(db, student_id):
    return getBy_Id(db,student_id) 



def remove_student(db, student_id):
    return delete_student(db, student_id)

def modify_student(db, student_id, student_data):
    return update_student(db, student_id, student_data)