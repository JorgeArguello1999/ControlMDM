# Schemas
from auth.schemas import UserCreate

# Encrypt 
import bcrypt

def add_user(user:UserCreate):
    hash_password = bcrypt.hashpw(
        user.password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    return {
        "name": user.name,
        "email": user.email,
        "password": hash_password
    }