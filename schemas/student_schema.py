from pydantic import BaseModel

class CreateStudent(BaseModel):
    student_name : str
    email :str
    phone :str