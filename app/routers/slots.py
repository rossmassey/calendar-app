from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from datetime import date
from app.schemas.slot import SlotResponse
from app.providers.base import BaseProvider
from app.dependencies import get_provider

router = APIRouter()


@router.get("/", response_model=List[SlotResponse])
async def get_available_slots(
    customer_id: str = Query(...),
    service_id: str = Query(...),
    date: date = Query(...),
    employee_id: str = Query(None),
    provider: BaseProvider = Depends(get_provider)
):
    """Get available slots"""
    slots = await provider.get_available_slots(customer_id, service_id, str(date), employee_id)
    return [
        SlotResponse(
            id=slot.id,
            center_id=slot.center_id,
            service_id=slot.service_id,
            date=slot.date,
            start_time=slot.start_time,
            end_time=slot.end_time,
            employee_id=slot.employee_id,
            price=slot.price,
            currency=slot.currency
        )
        for slot in slots
    ] 