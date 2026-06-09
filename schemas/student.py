from pydantic import BaseModel
class StudentCreate(BaseModel):
    name:str
    age:int
    faculty:str
class UpdateStudent(BaseModel):
    name:str
    age:int
    faculty:str    
class StudentResponse(BaseModel):
    id:int
    name:str
    age:int
    faculty:str
    class config:
        from_attribute=True
