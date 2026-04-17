from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class CourseCreate(BaseModel):
    title:       str
    description: Optional[str] = None
    thumbnail:   Optional[str] = None
    price:       float = 0.0
    is_free:     bool  = True
    level:       str   = "beginner"

class CourseUpdate(BaseModel):
    title:        Optional[str]   = None
    description:  Optional[str]   = None
    thumbnail:    Optional[str]   = None
    price:        Optional[float] = None
    is_free:      Optional[bool]  = None
    level:        Optional[str]   = None
    is_published: Optional[bool]  = None

class CourseOut(BaseModel):
    id: UUID; title: str; description: Optional[str]; thumbnail: Optional[str]
    price: float; is_free: bool; level: str; instructor_id: str
    is_published: bool; created_at: datetime
    class Config: from_attributes = True

class LessonCreate(BaseModel):
    title: str; content: Optional[str] = None; video_url: Optional[str] = None
    order: int = 0; duration: int = 0; is_free: bool = False

class LessonOut(BaseModel):
    id: UUID; course_id: UUID; title: str; content: Optional[str]
    video_url: Optional[str]; order: int; duration: int; is_free: bool
    class Config: from_attributes = True

class EnrollmentOut(BaseModel):
    id: UUID; course_id: UUID; user_id: str
    progress: float; completed: bool; enrolled_at: datetime
    class Config: from_attributes = True
