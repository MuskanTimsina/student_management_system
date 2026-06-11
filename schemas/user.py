from pydantic import BaseModel
class UserCreate(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    class config:
        from_attributes=True 

class UserLogin(BaseModel):
    username:str
    password:str 