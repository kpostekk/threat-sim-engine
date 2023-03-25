from pydantic import BaseModel


class NetworkDevice(BaseModel):
    mac_address: str
    ip_address: str
    netmask: str
    gateway: str
    dns: str
