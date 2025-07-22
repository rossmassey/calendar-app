from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.center import CenterResponse
from app.providers.base import BaseProvider
from app.dependencies import get_provider

router = APIRouter()


@router.get("/{center_id}", response_model=CenterResponse)
async def get_center(
    center_id: str,
    provider: BaseProvider = Depends(get_provider)
):
    """Get a center"""
    # Note: Centers not implemented in base provider yet
    return CenterResponse(
        id=center_id,
        center_name="Downtown Spa",
        zip_code="10001",
        time_zone="America/New_York"
    )


@router.get("/", response_model=List[CenterResponse])
async def get_all_centers(
    provider: BaseProvider = Depends(get_provider)
):
    """Get all centers"""
    return [
        CenterResponse(
            id="1",
            center_name="Downtown Spa",
            zip_code="10001",
            time_zone="America/New_York"
        )
    ] 