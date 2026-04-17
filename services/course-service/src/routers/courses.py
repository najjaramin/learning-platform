from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from src.database.db import get_db
from src.models.course import Course
from src.schemas.course import CourseCreate, CourseUpdate, CourseOut
import jwt, os

router = APIRouter()

def get_user_id(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token manquant")
    try:
        payload = jwt.decode(authorization.split(" ")[1], os.getenv("JWT_SECRET"), algorithms=["HS256"])
        return payload.get("id")
    except:
        raise HTTPException(status_code=401, detail="Token invalide")

@router.get("/", response_model=List[CourseOut])
def list_courses(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Course).filter(Course.is_published == True).offset(skip).limit(limit).all()

@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: str, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course: raise HTTPException(status_code=404, detail="Cours non trouvé")
    return course

@router.post("/", response_model=CourseOut, status_code=201)
def create_course(data: CourseCreate, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    course = Course(**data.model_dump(), instructor_id=user_id)
    db.add(course); db.commit(); db.refresh(course)
    return course

@router.put("/{course_id}", response_model=CourseOut)
def update_course(course_id: str, data: CourseUpdate, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    course = db.query(Course).filter(Course.id == course_id, Course.instructor_id == user_id).first()
    if not course: raise HTTPException(status_code=404, detail="Cours non trouvé")
    for k, v in data.model_dump(exclude_none=True).items(): setattr(course, k, v)
    db.commit(); db.refresh(course)
    return course

@router.delete("/{course_id}", status_code=204)
def delete_course(course_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    course = db.query(Course).filter(Course.id == course_id, Course.instructor_id == user_id).first()
    if not course: raise HTTPException(status_code=404, detail="Cours non trouvé")
    db.delete(course); db.commit()
