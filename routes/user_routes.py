from fastapi import APIRouter
from fastapi import HTTPException,status
from service import user_service
from schemas.user import UserCreate,UserResponse
router=APIRouter()
@router.post("/signup",response_model=UserResponse)
def signup(user:UserCreate):
    try:
      new_user=user_service.create_user_service(user)
      return new_user
    except Exception:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                           detail="something went wrong")

