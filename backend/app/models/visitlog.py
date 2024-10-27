from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

Base = declarative_base() #Base: SQLAlchemy의 선언적 기본 클래스입니다.

# SQLAlchemy ORM 모델
class VisitLog(Base):
    __tablename__ = 'visitlogs_visitlog'

    visitlog_id = Column(Integer, primary_key=True, index=True) #Column: SQLAlchemy의 컬럼 정의입니다.
    nfc_uid = Column(String(30), nullable=True)
    enter_time = Column(DateTime(timezone=True), nullable=False)
    exit_time = Column(DateTime(timezone=True), nullable=True)
    fields = Column(String(100), nullable=True)
    member_id = Column(Integer, ForeignKey('gyms_gymmember.member_id'), nullable=False)
    member = relationship("GymMember", back_populates="visitlogs") # relationship: 다른 테이블과의 관계를 설정합니다.

# Pydantic 모델
'''
Pydantic 모델 (VisitLogCreate, VisitLogResponse):
'''
class VisitLogCreate(BaseModel): # BaseModel: Pydantic의 기본 모델입니다. 클라이언트로부터 입력받을 데이터와 응답할 데이터를 정의합니다.
    nfc_uid: Optional[str] = None
    enter_time: datetime
    exit_time: Optional[datetime] = None
    fields: Optional[str] = None
    member_id: int

class VisitLogResponse(BaseModel):
    visitlog_id: int
    nfc_uid: Optional[str]
    enter_time: datetime
    exit_time: Optional[datetime]
    fields: Optional[str]
    member_id: int

    class Config:
        orm_mode = True # orm_mode: SQLAlchemy ORM 객체를 Pydantic 모델로 변환할 수 있게 해줍니다.

