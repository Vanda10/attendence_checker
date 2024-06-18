from pydantic import BaseModel
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

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