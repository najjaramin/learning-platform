from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.database.db import Base
import uuid, datetime

class Enrollment(Base):
    __tablename__ = "enrollments"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id   = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    user_id     = Column(String(100), nullable=False)
    progress    = Column(Float, default=0.0)
    completed   = Column(Boolean, default=False)
    enrolled_at = Column(DateTime, default=datetime.datetime.utcnow)
    course      = relationship("Course", back_populates="enrollments")
