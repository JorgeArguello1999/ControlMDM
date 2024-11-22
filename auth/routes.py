from fastapi import APIRouter

router = APIRouter()

# List User
@router.get('/')
def get_users():
    return {
        "user": "Jorge"
    }

# Add User
@router.post('/')
def post_user(user:dict):
    return user

# Delete User
@router.delete('/')
def delete_user(user:dict):
    return user