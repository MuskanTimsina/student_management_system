from fastapi import APIRouter
from fastapi import HTTPException,status
from service import user_service
from schemas.user import UserCreate,UserResponse,UserLogin
from auth import jwt_handler
router=APIRouter()
@router.post("/signup",response_model=UserResponse)
def signup(user:UserCreate):
    try:
      new_user=user_service.create_user_service(user)
      return new_user
    except Exception:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                           detail="something went wrong")

@router.post("/login")
def login(user_data:UserLogin):
   
   db_user=user_service.login_user_service(user_data)
   if db_user is None:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                          detail="Invalid username or password")
   token= jwt_handler.create_access_token({"username":db_user.username})
   return{
      "accesstoken":token,
      "token_type":"bearer"
   }
  