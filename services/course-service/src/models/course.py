from sqlalchemy import Column, String, Text, Float, Boolean, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.database.db import Base
import uuid, datetime, enum

class LevelEnum(str, enum.Enum):
    beginner     = "beginner"
    intermediate = "intermediate"
    advanced     = "advanced"

class Course(Base):
    __tablename__ = "courses"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title         = Column(String(200), nullable=False)
    description   = Column(Text, nullable=True)
    thumbnail     = Column(String(500), nullable=True)
    price         = Column(Float, default=0.0)
    is_free       = Column(Boolean, default=True)
    level         = Column(Enum(LevelEnum), default=LevelEnum.beginner)
    instructor_id = Column(String(100), nullable=False)
    is_published  = Column(Boolean, default=False)
    created_at    = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at    = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    lessons       = relationship("Lesson",     back_populates="course", cascade="all, delete-orphan")
    enrollments   = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")
