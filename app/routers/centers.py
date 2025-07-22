from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.center import CenterCreate
from app.schemas.center import CenterResponse
from app.providers.test_provider import TestProvider
from app.dependencies import get_provider

router = APIRouter()


@router.get("/{center_id}", response_model=CenterResponse)
async def get_center(
    center_id: str,
    provider: TestProvider = Depends(get_provider)
):
    """Get a center"""
    center = await provider.get_center(center_id)
    if not center:
        raise HTTPException(status_code=404, detail="Center not found")
    return CenterResponse(
        id=center.id,
        center_name=center.center_name,
        zip_code=center.zip_code,
        time_zone=center.time_zone
    )


@router.get("/", response_model=List[CenterResponse])
async def get_all_centers(
    provider: TestProvider = Depends(get_provider)
):
    """Get all centers"""
    centers = await provider.get_all_centers()
    return [
        CenterResponse(
            id=center.id,
            center_name=center.center_name,
            zip_code=center.zip_code,
            time_zone=center.time_zone
        )
        for center in centers
    ]


@router.post("/", response_model=CenterResponse)
async def create_center(
    center: CenterCreate,
    provider: TestProvider = Depends(get_provider)
):
    """Create a center (dummy route for provider=test)"""
    result = await provider.create_center(center)
    return CenterResponse(
        id=result.id,
        center_name=result.center_name,
        zip_code=result.zip_code,
        time_zone=result.time_zone
    ) 