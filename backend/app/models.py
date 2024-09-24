# 데이터베이스 모델을 정의
from sqlalchemy import Column, Integer, String
from .database import Base as DatabaseBase

class Item(DatabaseBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)