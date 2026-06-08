from sqlalchemy import Column,Integer,String
from Database import Base
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    faculty=Column(String,nullable=False)