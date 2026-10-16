from sqlalchemy import Column, Integer, String
from database.connection import Base

class Exam(Base):
    __tablename__="exams"

    exam_id=Column(Integer, primary_key=True)

    exam_name = Column(String(100))

    exam_type= Column(String(50))

    total_marks= Column(Integer)

    exam_date = Column(String(50))
