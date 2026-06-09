from Database import sessionlocal
from model.student import Student
def get_all_students_service():
    db=sessionlocal()
    students=db.query(Student).all()
    db.close()
    return students
def get_student_by_id_service(student_id):
    db=sessionlocal()
    student=db.query(Student).fileter(Student.id==student_id).first()
    db.close()
    return student
def create_student_service(student):
    db=sessionlocal()
    new_student=Student(
        name=student.name,
        age=student.age,
        faculty=student.faculty
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    return new_student
def delete_student_service(student_id):
    db=sessionlocal()
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
        db.close()
        return None
    db.delete(student)
    db.commit()
    db.close()
    return student
def update_Student_service(student_id:int,student_data):
    db=sessionlocal()
    student=db.query(Student).filter(Student.id==student_id).first()
    if student is None:
        db.close()
        return None
    student.name=student_data.name
    student.age=student_data.age
    student.faculty=student_data.faculty
    db.commit()
    db.refresh(student)
    db.close()
    return student