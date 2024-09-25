# Pydantic 모델을 정의하는 파일
# API 요청 및 응답의 데이터 구조를 정의함
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True