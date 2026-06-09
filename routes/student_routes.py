# apirouter is a tool used to organize api endpoint into separate files.
from fastapi import APIRouter
from schemas.student import StudentCreate,StudentResponse
from schemas.student import UpdateStudent
from fastapi import HTTPException,status
from service import student_service

router=APIRouter()

@router.post("/students",response_model=StudentResponse)
def create_student(student:StudentCreate):
   try:
    new_student=student_service.create_student_service(student)
    return new_student
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong")
    
@router.get("/students",response_model=list[StudentResponse])
def get_all_students():
   try:
      students=student_service.get_all_students_service()
      return students
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                       detail="Something went wrong !")
   
@router.get("/students/{student_id}",response_model=StudentResponse)
def get_one_student(student_id:int):
   try:
      student=student_service.get_student_by_id_service(student_id)
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong !")
   if student:
      return student
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail="student not found")   
@router.put("/students/{student_id}",response_model=StudentResponse)
def update_student(student_id:int,student:UpdateStudent):
   try:
     updated_student=student_service.update_Student_service(student_id,student)
   except Exception as e:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=str(e))
   if updated_student:
      return updated_student
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail="student not found")
   

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        deleted_id = student_service.delete_student_service(student_id)

        if deleted_id:
            return {
                "message": "STUDENT DELETED SUCCESSFULLY",
                "deleted_student_id": deleted_id
            }

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="student not found"
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="something went wrong"
        )
    
    
    
    