from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.database.db import Base
import uuid, datetime

class Lesson(Base):
    __tablename__ = "lessons"
    id        = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    title     = Column(String(200), nullable=False)
    content   = Column(Text, nullable=True)
    video_url = Column(String(500), nullable=True)
    order     = Column(Integer, default=0)
    duration  = Column(Integer, default=0)
    is_free   = Column(Boolean, default=False)
    created_at= Column(DateTime, default=datetime.datetime.utcnow)
    course    = relationship("Course", back_populates="lessons")
