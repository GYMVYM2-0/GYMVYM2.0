# gym 모델 정의
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from datetime import date

from backend.app.database import Base

class Gym(Base):
    __tablename__ = "gyms_gym"

    # gym_id = Column(Integer, primary_key=True, index=True)
    gym_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gym_name = Column(String, nullable=False)
    gym_address = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users_user.user_id"), nullable=False)

    # owner = relationship("User", back_populates="gyms")
    owner = relationship("User", back_populates="gyms")

class Gym(BaseModel):
    gym_id: int
    gym_name = str
    gym_address: str
    owner_id: int 

class GymMemberBase(BaseModel):
    join_date: date
    membership_type: str
    expiry_date: date = None
    recent_joined_date: date = None
    recent_membership: str = None
    recent_expiry: date = None
    renewal_status: bool = None
    renewal_count: int
    gym_id: int
    user_id: UUID

class GymMemberCreate(GymMemberBase):
    pass

class GymMember(GymMemberBase):
    member_id: int

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환 가능하도록 설정