from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

Base = declarative_base()

# 기존 Equipment 모델
class Equipment(Base):
    __tablename__ = 'equipment_equipment'

    equipment_id = Column(Integer, primary_key=True, index=True)
    equipment_name = Column(String(50), nullable=False)
    equipment_type = Column(String(50), nullable=False)
    equipment_description = Column(String, nullable=True)
    equipment_image = Column(String(100), nullable=True)
    gym_id = Column(Integer, ForeignKey('gyms_gym.gym_id'), nullable=False)
    user_id = Column(UUID, ForeignKey('account_customuser."user"'), nullable=True)

    gym = relationship("Gym", back_populates="equipments")
    user = relationship("CustomUser", back_populates="equipments")

# EquipmentInUse 모델
class EquipmentInUse(Base):
    __tablename__ = 'equipment_equipmentinuse'

    use_equip_id = Column(Integer, primary_key=True, index=True)
    start_time = Column(TIMESTAMP(timezone=True), nullable=True)
    end_time = Column(TIMESTAMP(timezone=True), nullable=True)
    equipment_id = Column(Integer, ForeignKey('equipment_equipment.equipment_id'), nullable=False)
    user_id = Column(UUID, ForeignKey('account_customuser."user"'), nullable=False)
    res_id = Column(Integer, ForeignKey('equipment_equipmentreservation.res_id'), nullable=True)

    equipment = relationship("Equipment")
    user = relationship("CustomUser")
    reservation = relationship("EquipmentReservation")

# EquipmentReservation 모델
class EquipmentReservation(Base):
    __tablename__ = 'equipment_equipmentreservation'

    res_id = Column(Integer, primary_key=True, index=True)
    res_start_time = Column(TIMESTAMP(timezone=True), nullable=True)
    res_end_time = Column(TIMESTAMP(timezone=True), nullable=True)
    equipment_id = Column(Integer, ForeignKey('equipment_equipment.equipment_id'), nullable=False)
    user_id = Column(UUID, ForeignKey('account_customuser."user"'), nullable=True)
    time_slot_id = Column(Integer, ForeignKey('equipment_timeslot.timeslot_id'), nullable=False)

    equipment = relationship("Equipment")
    user = relationship("CustomUser")

# EquipmentTimeSlot 모델
class EquipmentTimeSlot(Base):
    __tablename__ = 'equipment_timeslot'

    timeslot_id = Column(Integer, primary_key=True, index=True) # timeslot_id: 기본 키로 사용되는 식별자
    slot = Column(String(20), nullable=False) # slot: 시간 슬롯을 저장하는 필드

    __table_args__ = (UniqueConstraint('slot', name='equipment_timeslot_slot_key'),) # UniqueConstraint: slot 필드에 대한 유일 제약 조건을 설정함

# Pydantic 모델
class EquipmentTimeSlotCreate(BaseModel): # EquipmentTimeSlotCreate: 시간 슬롯 생성을 위한 입력 모델
    slot: str

class EquipmentTimeSlotResponse(BaseModel): # EquipmentTimeSlotResponse: 시간 슬롯 응답 모델로, 데이터베이스에서 반환되는 데이터를 정의
    timeslot_id: int
    slot: str

    class Config:
        orm_mode = True # orm_mode: SQLAlchemy ORM 객체를 Pydantic 모델로 변환할 수 있게 해줌
