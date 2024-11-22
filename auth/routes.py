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
from auth.schemas import UserCreate

router = APIRouter()

# List User
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(con_database)):
    users = db.query(User).all()
    return users

# Add User
@router.post('/', response_model=list(UserResponse))
def post_user(user: UserCreate, db: Session = Depends(con_database)):
    # User exist? 
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=200, detail="Your Email alredy registered")
    
    # Save new user
    return user

# Delete User
@router.delete('/')
def delete_user(user:dict):
    return user