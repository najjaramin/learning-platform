from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.db import engine, Base
from src.routers import courses, lessons, enrollments

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Service", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(courses.router,     prefix="/api/courses",     tags=["courses"])
app.include_router(lessons.router,     prefix="/api/lessons",     tags=["lessons"])
app.include_router(enrollments.router, prefix="/api/enrollments", tags=["enrollments"])

@app.get("/health")
def health(): return {"status": "ok", "service": "course-service"}
