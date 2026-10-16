from models.exam_model import Exam
def save_exam(db,exam):
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam

def get_all_exams(db):
    return db.query(Exam).all()


def get_exam_by_id(db, exam_id):
    return db.query(Exam).filter(
        Exam.exam_id == exam_id
    ).first()

def update_exam(db):
    db.commit()


def delete_exam(db, exam):
    db.delete(exam)
    db.commit()