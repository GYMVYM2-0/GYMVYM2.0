# Pydantic 모델을 정의하는 파일
# API 요청 및 응답의 데이터 구조를 정의함
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True