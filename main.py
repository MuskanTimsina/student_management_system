from fastapi import FastAPI
from routes.student_routes import router as student_router
from Database import engine,Base
app=FastAPI()
app.include_router(student_router)
Base.metadata.create_all(bind=engine)
