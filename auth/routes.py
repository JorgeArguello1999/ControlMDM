from fastapi import APIRouter, Depends

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

router = APIRouter()

# List User
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(con_database)):
    users = db.query(User).all()
    return users

# Add User
@router.post('/')
def post_user(user:dict):
    return user

# Delete User
@router.delete('/')
def delete_user(user:dict):
    return user