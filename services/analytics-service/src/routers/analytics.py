from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.database import get_db
from src.models.event import Event
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class EventCreate(BaseModel):
    event_type: str
    user_id:    Optional[str] = None
    course_id:  Optional[str] = None
    data:       Optional[dict] = None

@router.post("/event", status_code=201)
def track_event(payload: EventCreate, db: Session = Depends(get_db)):
    event = Event(**payload.model_dump())
    db.add(event); db.commit()
    return {"message": "Événement enregistré"}

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return {
        "total_events":      db.query(func.count(Event.id)).scalar(),
        "total_enrollments": db.query(func.count(Event.id)).filter(Event.event_type == "enrollment").scalar(),
        "total_completions": db.query(func.count(Event.id)).filter(Event.event_type == "completion").scalar(),
        "total_feedbacks":   db.query(func.count(Event.id)).filter(Event.event_type == "feedback").scalar(),
    }

@router.get("/course/{course_id}")
def course_stats(course_id: str, db: Session = Depends(get_db)):
    events = db.query(Event).filter(Event.course_id == course_id).all()
    return {
        "course_id":    course_id,
        "total_events": len(events),
        "events": [{"type": e.event_type, "created_at": str(e.created_at)} for e in events],
    }
