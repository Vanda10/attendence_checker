from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from database.database import engine
from sqlalchemy.ext.declarative import declarative_base
from controller.controller import router as class_router
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

app.include_router(class_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
