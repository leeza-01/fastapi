from models.course_model import Course


def save_course(db, course):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def get_all_courses(db):
    return db.query(Course).all()


def get_course_by_id(db, course_id):
    return db.query(Course).filter(
        Course.course_id == course_id
    ).first()


def update_course(db, course_id, course_data):

    course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    if course:
        course.course_name = course_data.course_name
        course.duration = course_data.duration
        course.fees = course_data.fees

        db.commit()
        db.refresh(course)

    return course


def delete_course(db, course_id):

    course = db.query(Course).filter(
        Course.course_id == course_id
    ).first()

    if course:
        db.delete(course)
        db.commit()

    return course