from typing import List
from pydantic import BaseModel
from datetime import datetime, time


class BookingResponse(BaseModel):
    id: str
    slot_id: str
    status: str
    expires_at: datetime


class BookingDetailResponse(BaseModel):
    id: str
    status: str
    service_id: str
    employee_id: str
    start_time: time
    end_time: time


class BookingListResponse(BaseModel):
    bookings: List[BookingDetailResponse]
    total: int 