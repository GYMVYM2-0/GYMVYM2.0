from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import DeclarativeMeta
import uuid
from fastapi_users import FastAPIUsers, BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database import Base, SessionLocal
from fastapi_users.authentication import JWTStrategy

class UserTable(SQLAlchemyBaseUserTable, Base):
    __tablename__ = "account_customuser"

    # 필드 정의
    is_superuser = Column(Boolean, nullable=False)
    user = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nfc_uid = Column(String, unique=True, nullable=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    detail_address = Column(String(100), nullable=False)
    nickname = Column(String(100), unique=True, nullable=False)
    user_image = Column(String(100), nullable=True)
    birth = Column(Date, nullable=False)
    usertype = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)
    date_joined = Column(DateTime(timezone=True), nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, phone_number={self.phone_number})>"

# 유저 데이터베이스 설정
async def get_user_db(session: AsyncSession):
    yield SQLAlchemyUserDatabase(session, UserTable)

# FastAPI-Users 매니저 설정
class UserManager(UUIDIDMixin, BaseUserManager[UserTable, uuid.UUID]):
    user_db: SQLAlchemyUserDatabase

# FastAPI-Users 설정
fastapi_users = FastAPIUsers[UserTable, uuid.UUID](
    UserManager(get_user_db),
    [JWTStrategy(secret="SECRET", lifetime_seconds=3600)],
)


# 데이터베이스 모델을 정의
# from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.ext.declarative import declarative_base
# import uuid

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "account_customuser"

#     # 필드 정의
#     is_superuser = Column(Boolean, nullable=False)
#     user = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     nfc_uid = Column(String, unique=True, nullable=True)
#     username = Column(String(100), unique=True, nullable=False)
#     password = Column(String(100), nullable=False)
#     phone_number = Column(String(15), unique=True, nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     address = Column(String(100), nullable=False)
#     detail_address = Column(String(100), nullable=False)
#     nickname = Column(String(100), unique=True, nullable=False)
#     user_image = Column(String(100), nullable=True)
#     birth = Column(Date, nullable=False)
#     usertype = Column(Integer, nullable=False)
#     gender = Column(String(1), nullable=False)
#     date_joined = Column(DateTime(timezone=True), nullable=False)
#     last_login = Column(DateTime(timezone=True), nullable=True)

#     def __repr__(self):
#         return f"<User(username={self.username}, email={self.email}, phone_number={self.phone_number})>"
