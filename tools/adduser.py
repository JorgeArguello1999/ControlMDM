# Schemas
from auth.schemas import UserCreate

# Encrypt password
from tools import encrypt

def add_user(user:UserCreate):
    return {
        "name": user.name,
        "email": user.email,
        "password": encrypt.encrypt_password(user.password)
    }