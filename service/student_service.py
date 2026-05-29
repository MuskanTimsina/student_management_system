from Database import get_connection
from fastapi import HTTPException,status

def get_all_students_service():
    
        conn,cursor=get_connection()
        cursor.execute("SELECT * FROM students")
        students=cursor.fetchone()
        conn.close()
        return students

def get_one_student_service(student_id):
        conn,cursor=get_connection()
        cursor.execute("SELECT * FROM students WHERE id=%s",(student_id,))
        student=cursor.fetchone()
        conn.close()
        return student

def create_student_service(student):
        conn,cursor=get_connection()
        cursor.execute("INSERT INTO students(id,name,age,faculty) VALUES(%s,%s,%s,%s) returning *",
                       (student.id,student.name,student.age,student.faculty))
        new_student=cursor.fetchone()
        conn.commit()
        conn.close()
        return new_student

def update_student_service(student_id,student):
        conn,cursor=get_connection()
        cursor.execute("UPDATE students SET name=%s,age=%s,faculty=%s WHERE id=%s",
                       (student.name,student.age,student.faculty,student_id))
        updated_student=cursor.fetchone()
        conn.commit()
        conn.close()
        return updated_student
def delete_student_service(student_id):
        conn,cursor=get_connection()
        cursor.execute("DELETE FROM students where id = %s returning *",(student_id,))
        deleted_Student=cursor.fetchone()
        conn.commit()
        conn.close()
        return deleted_Student

