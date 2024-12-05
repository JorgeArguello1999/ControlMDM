from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tools.database import Base  

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, nullable=False, index=True)
    location = Column(String, nullable=False)
    red_name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    wifi_ssid = Column(String, nullable=True)
    os_version = Column(String, nullable=False)

    # User relation
    user_devices = relationship("UserDevice", back_populates="device")

class UserDevice(Base):
    __tablename__ = "user_devices"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_auth.id"), nullable=False)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)

    # Relations
    user = relationship("User", back_populates="user_devices")
    device = relationship("Device", back_populates="user_devices")
