from fastapi import APIRouter, HTTPException, Depends
from app.models.booking import BookingCreate
from app.schemas.booking import BookingResponse, BookingDetailResponse
from app.providers.base import BaseProvider
from app.dependencies import get_provider

router = APIRouter()


@router.post("/", response_model=BookingResponse)
async def create_booking(
    booking: BookingCreate,
    provider: BaseProvider = Depends(get_provider)
):
    """Create a booking"""
    result = await provider.create_booking(booking)
    return BookingResponse(
        id=result.id,
        slot_id=result.slot_id,
        status=result.status,
        expires_at=result.expires_at
    )


@router.get("/{booking_id}", response_model=BookingDetailResponse)
async def get_booking(
    booking_id: str,
    provider: BaseProvider = Depends(get_provider)
):
    """Get a booking"""
    booking = await provider.get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return BookingDetailResponse(
        id=booking.id,
        status=booking.status,
        service_id=booking.service_id,
        employee_id=booking.employee_id,
        start_time=booking.start_time,
        end_time=booking.end_time
    ) 