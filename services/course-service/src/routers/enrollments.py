from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from src.database.db import get_db
from src.models.enrollment import Enrollment
from src.schemas.course import EnrollmentOut
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

@router.post("/{course_id}", response_model=EnrollmentOut, status_code=201)
def enroll(course_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    exists = db.query(Enrollment).filter(Enrollment.course_id == course_id, Enrollment.user_id == user_id).first()
    if exists: raise HTTPException(status_code=409, detail="Déjà inscrit")
    enrollment = Enrollment(course_id=course_id, user_id=user_id)
    db.add(enrollment); db.commit(); db.refresh(enrollment)
    return enrollment

@router.get("/my", response_model=List[EnrollmentOut])
def my_enrollments(db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    return db.query(Enrollment).filter(Enrollment.user_id == user_id).all()

@router.patch("/{course_id}/progress")
def update_progress(course_id: str, progress: float, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    enrollment = db.query(Enrollment).filter(Enrollment.course_id == course_id, Enrollment.user_id == user_id).first()
    if not enrollment: raise HTTPException(status_code=404, detail="Inscription non trouvée")
    enrollment.progress  = min(progress, 100.0)
    enrollment.completed = enrollment.progress >= 100.0
    db.commit()
    return {"message": "Progression mise à jour", "progress": enrollment.progress}
