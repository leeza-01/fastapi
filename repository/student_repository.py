from models.student_model import Student

def save_student(db , student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student