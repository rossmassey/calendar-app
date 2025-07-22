from pydantic import BaseModel
from decimal import Decimal


class ServiceBase(BaseModel):
    service_name: str
    price: Decimal
    duration: int  # in minutes


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    pass


class Service(ServiceBase):
    id: str
    
    class Config:
        from_attributes = True 