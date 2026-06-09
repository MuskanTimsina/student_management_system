from fastapi import FastAPI
from routes.student_routes import router as student_router
from model.student import Student
from model.user import User
from Database import engine,Base
app=FastAPI()
app.include_router(student_router)
Base.metadata.create_all(bind=engine)
