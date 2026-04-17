from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.db import get_db
from src.models.lesson import Lesson
from src.schemas.course import LessonCreate, LessonOut

router = APIRouter()

@router.get("/course/{course_id}", response_model=List[LessonOut])
def get_lessons(course_id: str, db: Session = Depends(get_db)):
    return db.query(Lesson).filter(Lesson.course_id == course_id).order_by(Lesson.order).all()

@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: str, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson: raise HTTPException(status_code=404, detail="Leçon non trouvée")
    return lesson

@router.post("/course/{course_id}", response_model=LessonOut, status_code=201)
def create_lesson(course_id: str, data: LessonCreate, db: Session = Depends(get_db)):
    lesson = Lesson(**data.model_dump(), course_id=course_id)
    db.add(lesson); db.commit(); db.refresh(lesson)
    return lesson

@router.delete("/{lesson_id}", status_code=204)
def delete_lesson(lesson_id: str, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson: raise HTTPException(status_code=404, detail="Leçon non trouvée")
    db.delete(lesson); db.commit()
