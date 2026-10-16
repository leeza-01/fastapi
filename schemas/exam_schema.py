from pydantic import BaseModel

class CreateExam(BaseModel):

    exam_name: str
    exam_type: str
    total_marks: int
    exam_date: str