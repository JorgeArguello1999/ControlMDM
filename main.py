from fastapi import FastAPI

# Routes 
from auth.routes import router as auth_router
from MDM.routes import router as mdm_router

# Database
from tools.database import Base, engine
from auth.models import User

# Env
from dotenv import load_dotenv
from os import getenv
load_dotenv()

app = FastAPI()

# Registering routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(mdm_router, prefix="/mdm", tags=["MDM"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

# LOGs
print(f"DATABASE: {getenv('DATABASE_URL')}")

# Create Database
Base.metadata.create_all(bind=engine)