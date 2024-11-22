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
        orm_mode = True

# Update User
class UpdateUser(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None 