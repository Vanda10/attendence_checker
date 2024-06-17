from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List, Annotated
from database.database import engine
from sqlalchemy.ext.declarative import declarative_base
from controller.controller import router as class_router

Base = declarative_base()

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(class_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
