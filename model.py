import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, time

Base = declarative_base()

class SessionModel(Base):
    __tablename__ = 'sessions'
    
    session_id = Column(Integer, primary_key=True, index=True)
    session_date = Column(DateTime)
    session_start_time = Column(DateTime)
    session_end_time = Column(DateTime)
    session_name = Column(String, index=True)
    class_code = Column(String, index=True)
    

# Pydantic models
class SessionBase(BaseModel):
    session_date: datetime
    session_start_time: time
    session_end_time: time
    session_name: str
    class_code: str

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types like datetime

class SessionInfo(SessionBase):
    session_id: int

    class Config:
        from_attributes = True


class user(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_role = Column(String, index=True)
    user_name = Column(String, index=True)
    class_code = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    dob = Column(String, index=True)


class AttendanceRecord(Base):
    __tablename__ = 'attendance_records'

    attendance_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    session_id = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime)

class AttendanceRequest(BaseModel):
    user_id: int
    session_id: int
    timestamp: datetime