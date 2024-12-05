from fastapi import HTTPException
from fastapi import APIRouter
from fastapi import Depends

# Database
from tools.database import SessionLocal
from sqlalchemy.orm import Session

# Create database connection
def con_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas
from MDM.schemas import DeviceResponse

# Tools
router = APIRouter()

# List User
@router.get("/", response_model=list[DeviceResponse])
def get_users(db: Session = Depends(con_database)):
    devices = db.query(DeviceResponse).all()
    return devices 

