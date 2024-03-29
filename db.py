from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Initialize sqlite database engine and connect to a database file
engine = create_engine(
    "sqlite:///attendance.db"
)

Base = declarative_base()

# Class mapped to table, attributes map to colum
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_num = Column(String(255))
    name = Column(String(255))
    imageName = Column(String(255))

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_num = Column(String(255))
    name = Column(String(255))
    date = Column(String(255))
    time = Column(String(255))

# Only run once to create tables
# Base.metadata.tables['student'].create(engine)
# Base.metadata.tables['attendance'].create(engine)

# Open session to database
Session = sessionmaker(bind=engine)
session = Session()
def insertStudent(student):
    # query database by filtering on the attribute
    qry_object = session.query(Student).filter(Student.student_num == student.student_num).all()

    if qry_object:
        print('student already registered')
        return
    # insert the record
    session.add(student)
    session.commit()

def getAllStudents():
    return session.query(Student).all()

def insertAttendance(attendance):

    qry_object = session.query(Attendance).filter(Attendance.student_num == attendance.student_num).all()

    if qry_object:
        print(f'student {attendance.student_num} {attendance.name} already registered')
        return
    session.add(attendance)
    session.commit()

def queryAllAttendance():
    return session.query(Attendance).all()

def deleteAllAttendance():
    session.query(Attendance).delete()
    session.commit()

def deleteAllStudents():
    session.query(Student).delete()
    session.commit()