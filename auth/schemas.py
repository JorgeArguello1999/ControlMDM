from pydantic import BaseModel

# Create User Struct
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# Response User
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

# Update User
class UpdateUser(BaseModel):
    name: str | None = None
    email: str | None = None
    old_password: str | None = None 
    new_password: str | None = None