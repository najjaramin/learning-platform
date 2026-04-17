from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from src.database import Base
import uuid, datetime

class Event(Base):
    __tablename__ = "analytics_events"
    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type = Column(String(100), nullable=False)
    user_id    = Column(String(100), nullable=True)
    course_id  = Column(String(100), nullable=True)
    data       = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
