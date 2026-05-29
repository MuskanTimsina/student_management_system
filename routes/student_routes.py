# apirouter is a tool used to organize api endpoint into separate files.
from fastapi import APIRouter
from schemas.student import studentcreate
from schemas.student import updatestudent
from Database import  get_connection
from fastapi import HTTPException,status
from service import student_service

router=APIRouter()

@router.post("/students")
def create_student(student:studentcreate):
   try:
    new_student=student_service.create_student_service(student)
    return{"message":".....STUDENT MANAGEMENT SYSTEM.....",
             "new_student":new_student}
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong")
    
@router.get("/students")
def get_all_students():
   try:
      students=student_service.get_all_students_service()
      return{"message":".....STUDENT MANAGEMENT SYSTEM.....","students":students}
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong")
   
@router.get("/students/{student_id}")
def get_one_student(student_id:int):
   try:
      student=student_service.get_one_student_service(student_id)
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong")
   if student:
      return{"messsage":".....STUDENT MANAGEMTN SYSTEM.....",
             "student":student}
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail=f"student not found with id={student_id}")   

@router.put("/students/{student_id}")
def update_student(student_id:int,student:updatestudent):
   try:
     updated_student=student_service.update_student_service(student_id,student)
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="something went wrong")
   if updated_student:
      return{"message":"STUDENT UPDATED SUCCESSULLY",
             "student":updated_student}
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail="student not found")
   
@router.delete("/students/{student_id}")
def delete_student(student_id:int):
   try:
      deleted_student=student_service.delete_student_service()
   except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail="something went wrong")
   if deleted_student:
      return{"message":"STUDENT DELETED SUCESSFULLY",
             "deleted_student":deleted_student}
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail="student not found")   

    
    
    
    