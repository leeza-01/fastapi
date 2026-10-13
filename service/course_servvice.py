from models.course_model import Course
from repository.course_repository import (
    save_course,
    get_all_courses,
    get_course_by_id,
    update_course,
    delete_course
)


def create_course(db, course_data):

    course = Course(
        course_name=course_data.course_name,
        duration=course_data.duration,
        fees=course_data.fees
    )

    return save_course(db, course)


def fetch_all_courses(db):
    return get_all_courses(db)


def fetch_course_by_id(db, course_id):
    return get_course_by_id(db, course_id)


def modify_course(db, course_id, course_data):
    return update_course(db, course_id, course_data)


def remove_course(db, course_id):
    return delete_course(db, course_id)