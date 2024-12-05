from fastapi import HTTPException
from fastapi import APIRouter
from fastapi import Depends

# Database
from sqlalchemy.orm import Session
from auth.models import User
from auth import models

# Create database connection
def con_database():
    db = models.localsession()
    try:
        yield db
    finally:
        db.close()

# Schemas
from auth.schemas import UserResponse
from auth.schemas import DeleteUser
from auth.schemas import UserCreate
from auth.schemas import UpdateUser

# Tools 
from tools import adduser
from tools import encrypt

router = APIRouter()

# List User
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(con_database)):
    users = db.query(User).all()
    return users

