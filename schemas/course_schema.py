from pydantic import BaseModel


class CourseCreate(BaseModel):
    course_name: str
    duration: str
    fees: int