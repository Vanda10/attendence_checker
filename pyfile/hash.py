from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from database.database import Base
from models.user import User  # Import your SQLAlchemy models
from auth.utils import hash_password  # Import your hash_password function

DATABASE_URL = "postgresql://postgres.fehhjfuqgebqrouognhl:vanda12410748@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def hash_existing_passwords():
    db = SessionLocal()
    users = db.query(User).all()

    for user in users:
        if user.password:
            hashed_password = hash_password(user.password)
            user.hashed_password = hashed_password
            user.password = None  # Optionally, clear the plain text password
            db.add(user)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    hash_existing_passwords()
