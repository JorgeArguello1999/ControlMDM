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

# Add User
@router.post('/', response_model=UserResponse)
def post_user(user: UserCreate, db: Session = Depends(con_database)):
    # User exist? 
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=200, detail="Your Email alredy registered")
    
    # Save new user
    try: 
        user = adduser.add_user(user)
        user = User(name=user['name'], email=user['email'], password=user['password'])
        db.add(user)
        db.commit()
        db.refresh(user)

    except Exception as e:
        raise HTTPException(status_code=200, detail=f'Problem with your data: {e}')

    return user 

# User Update
@router.put('/', response_model=UserResponse)
def put_user(user: UpdateUser, db: Session = Depends(con_database)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update User
    try:
        if not user.name and user.email and user.new_password and user.old_password:
            raise HTTPException(status_code=404, detail="Your data isn't correct")

        if encrypt.verify_password(user.old_password, db_user.password) != True: 
            raise HTTPException(status_code=404, detail="Old password isn't correct")

        if user.old_password == user.new_password: 
            raise HTTPException(status_code=200, detail="Your old password and the new password is the same")
        
        # Create class with new data
        db_user.id = db_user.id 
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = encrypt.encrypt_password(user.new_password)

        # Save the changes
        db.commit()
        db.refresh(db_user)

        return db_user          

    except Exception as e:
        raise HTTPException(status_code=200, detail=f"Problem with your data: {e}")


# Delete User
@router.delete('/', status_code=204)
def delete_user(user: DeleteUser, db: Session = Depends(con_database)):
    # Search the user
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user: raise HTTPException(status_code=4040, detail="User not found")

    # Password check 
    if not encrypt.verify_password(user.password, db_user.password): 
        raise HTTPException(status_code=403, detail="Incorrect Password")

    # Delete user
    try:
        db.delete(db_user)
        db.commit()

    except Exception as e:
        raise HTTPException(status_code=200, detail=f"Problem with process: {e}")
    
    return {"message": "User successfully deleted"}