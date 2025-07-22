from pydantic import BaseModel
from datetime import datetime, time


class BookingCreate(BaseModel):
    slot_id: str
    customer_id: str
    service_id: str
    employee_id: str
    center_id: str


class BookingResponse(BaseModel):
    id: str
    slot_id: str
    status: str
    expires_at: datetime


class BookingDetail(BaseModel):
    id: str
    status: str
    service_id: str
    employee_id: str
    start_time: time
    end_time: time
    
    class Config:
        from_attributes = True 