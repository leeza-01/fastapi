from models.student_model import Student

def save_student(db , student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def getallStudents(db):
    return db.query(Student).all()

def getBy_Id(db,student_id):
    return db.query(Student).filter(Student.student_id==student_id).first()

def delete_student(db, student_id):

    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()

    return student

def update_student(db, student_id, student_data):

    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if student:
        student.student_name = student_data.student_name
        student.email = student_data.email
        student.phone = student_data.phone

        db.commit()
        db.refresh(student)

    return student