from sqlalchemy import Column,Integer,String
from database.connection import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer , primary_key = True, index = True)

    student_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True)
    phone = Column(String(15))
    