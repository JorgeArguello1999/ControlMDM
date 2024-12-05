from pydantic import BaseModel

class DeviceResponse(BaseModel):
    token: str
    location: str | None = None
    red_name: str | None = None
    ip_address: str | None = None
    wifi_ssid: str | None = None
    os_version: str | None = None

    class Config:
        from_attributes = True

class UserDevicesResponse(BaseModel):
    devices: list[DeviceResponse]

    class Config:
        from_attributes = True