from pydantic import BaseModel
from datetime import date, time
from decimal import Decimal
from typing import Optional


class SlotQuery(BaseModel):
    customer: str
    service: str
    date: date
    employee: Optional[str] = None


class Slot(BaseModel):
    id: str
    center_id: str
    service_id: str
    date: date
    start_time: time
    end_time: time
    employee_id: str
    price: Decimal
    currency: str = "USD"
    
    class Config:
        from_attributes = True 