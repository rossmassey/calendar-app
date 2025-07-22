from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from datetime import date
from app.models.slot import SlotQuery
from app.schemas.slot import SlotResponse
from app.providers.test_provider import TestProvider
from app.dependencies import get_provider

router = APIRouter()


@router.get("/{slot_id}", response_model=SlotResponse)
async def get_slot(
    slot_id: str,
    provider: TestProvider = Depends(get_provider)
):
    """Get a slot"""
    slot = await provider.get_slot(slot_id)
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    return SlotResponse(
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


@router.get("/", response_model=List[SlotResponse])
async def get_available_slots(
    customer: str = Query(...),
    service: str = Query(...),
    date: date = Query(...),
    employee: str = Query(None),
    provider: TestProvider = Depends(get_provider)
):
    """Get all available slots for a specified service"""
    query = SlotQuery(
        customer=customer,
        service=service,
        date=date,
        employee=employee
    )
    slots = await provider.get_available_slots(query)
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