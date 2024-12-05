from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from tools.database import Base

# Model for users
class User(Base):
    __tablename__ = "user_auth"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Relations
    user_devices = relationship("UserDevice", back_populates="user")