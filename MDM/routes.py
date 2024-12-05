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
from MDM.schemas import UserDevicesResponse

# Models
from auth.models import User
from MDM.models import UserDevice 
from MDM.models import Device

# Tools
router = APIRouter()

# List User
@router.get("/users/{user_id}/devices", response_model=UserDevicesResponse)
def get_user_devices(user_id: int, db: Session = Depends(con_database)):
    # Find User
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Devices from user
    user_devices = (
        db.query(Device)
        .join(UserDevice, Device.id == UserDevice.device_id)
        .filter(UserDevice.user_id == user_id)
        .all()
    )
    
    return {"devices": user_devices}