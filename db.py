from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Initialize sqlite database engine
engine = create_engine(
    "sqlite:///attendance.db"
)

Base = declarative_base()

# Class for student table
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_num = Column(String(255))
    name = Column(String(255))
    imageName = Column(String(255))

# Class for attendance table
class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_num = Column(String(255))
    name = Column(String(255))
    date = Column(String(255))
    time = Column(String(255))

# Create tables
# Base.metadata.tables['student'].create(engine)
# Base.metadata.tables['attendance'].create(engine)