from typing import List
from pydantic import BaseModel
from datetime import date, time
from decimal import Decimal


class SlotResponse(BaseModel):
    id: str
    center_id: str
    service_id: str
    date: date
    start_time: time
    end_time: time
    employee_id: str
    price: Decimal
    currency: str


class SlotListResponse(BaseModel):
    slots: List[SlotResponse]
    total: int 