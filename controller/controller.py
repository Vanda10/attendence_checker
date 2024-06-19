from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.database as database  # Adjust the import path accordingly
from models.attendance_record import AttendanceRecord, AttendanceRequest
from models.session import SessionModel, SessionInfo
from typing import List
from datetime import date
from sqlalchemy import cast, Date


router = APIRouter()

@router.get("/sessions")
def get_sessions(db: Session = Depends(database.get_db)):
    return db.query(SessionModel).all()

@router.get("/session_name")
def get_session_name(db: Session = Depends(database.get_db)):
    sessions = db.query(SessionModel).all()
    session_info = [
        {
            "session_name": session.session_name,
            "session_date": session.session_date,
            "session_start_time": session.session_start_time
        }
        for session in sessions
    ]
    return session_info

@router.get("/sessions/by_class_code/{class_code}", response_model=List[SessionInfo])
def get_sessions_by_class_code(class_code: str, db: Session = Depends(database.get_db)):
    today = date.today()
    sessions = db.query(SessionModel).filter(SessionModel.class_code == class_code, cast(SessionModel.session_date, Date) >= today).all()
    if not sessions:
        raise HTTPException(status_code=404, detail="No upcoming sessions found for the provided class code")
    return sessions


@router.get("/sessions/{session_id}", response_model=SessionInfo)
def read_session(session_id: int, db: Session = Depends(database.get_db)):
    session = db.query(SessionModel).filter(SessionModel.session_id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.get("/attendance_record")
def get_attendance(db: Session = Depends(database.get_db)):
    return db.query(AttendanceRecord).all()

@router.post("/api/attendance/")
def create_attendance_record(attendance_request: AttendanceRequest, db: Session = Depends(database.get_db)):
    # Check if an attendance record already exists for the same user_id and session_id
    existing_record = db.query(AttendanceRecord).filter_by(
        user_id=attendance_request.user_id,
        session_id=attendance_request.session_id
    ).first()

    if existing_record:
        # If a record already exists, return a message indicating that attendance has already been recorded
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Attendance already recorded for this session and user."
        )

    # Create a new attendance record
    attendance_record = AttendanceRecord(
        user_id=attendance_request.user_id,
        session_id=attendance_request.session_id,
        timestamp=attendance_request.timestamp
    )
    db.add(attendance_record)
    db.commit()
    db.refresh(attendance_record)
    return {"status": "success", "attendance_id": attendance_record.attendance_id}
