from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from uuid import UUID

Base = declarative_base()

class SchedulerEvent(Base):
    __tablename__ = "scheduler_event"

    schedule_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    start = Column(TIMESTAMP(timezone=True), nullable=False)
    end = Column(TIMESTAMP(timezone=True), nullable=False)
    background_color = Column(String(20), nullable=False)
    user_id = Column(UUID, ForeignKey("account_customuser.user"), nullable=True)

    user = relationship("User", back_populates="events")

# Pydantic Models
class SchedulerEventBase(BaseModel):
    title: str
    start: str  # ISO format date string
    end: str    # ISO format date string
    background_color: str
    user_id: UUID = None

class SchedulerEventCreate(SchedulerEventBase):
    pass

class SchedulerEvent(SchedulerEventBase):
    schedule_id: int

    class Config:
        orm_mode = True
        