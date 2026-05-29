from pydantic import BaseModel
class studentcreate(BaseModel):
    id:int
    name:str
    age:int
    faculty:str

class updatestudent(BaseModel):
    name:str
    age:int
    faculty:str    