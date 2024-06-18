from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_role = Column(String, index=True)
    user_name = Column(String, index=True)
    class_code = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    dob = Column(String, index=True)

#Schemas for pydantic model
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
