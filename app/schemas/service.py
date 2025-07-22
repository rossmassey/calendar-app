from typing import List
from pydantic import BaseModel
from decimal import Decimal


class ServiceResponse(BaseModel):
    id: str
    service_name: str
    price: Decimal
    duration: int


class ServiceListResponse(BaseModel):
    services: List[ServiceResponse]
    total: int 