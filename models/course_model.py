from sqlalchemy import Column, Integer, String
from database.connection import Base


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)

    course_name = Column(String(100))

    duration = Column(String(50))

    fees = Column(Integer)
    