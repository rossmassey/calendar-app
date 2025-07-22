from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.service import ServiceCreate
from app.schemas.service import ServiceResponse
from app.providers.test_provider import TestProvider
from app.dependencies import get_provider

router = APIRouter()


@router.get("/{service_id}", response_model=ServiceResponse)
async def get_service(
    service_id: str,
    provider: TestProvider = Depends(get_provider)
):
    """Get a service"""
    service = await provider.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return ServiceResponse(
        id=service.id,
        service_name=service.service_name,
        price=service.price,
        duration=service.duration
    )


@router.get("/", response_model=List[ServiceResponse])
async def get_all_services(
    provider: TestProvider = Depends(get_provider)
):
    """Get all services"""
    services = await provider.get_all_services()
    return [
        ServiceResponse(
            id=service.id,
            service_name=service.service_name,
            price=service.price,
            duration=service.duration
        )
        for service in services
    ]


@router.post("/", response_model=ServiceResponse)
async def create_service(
    service: ServiceCreate,
    provider: TestProvider = Depends(get_provider)
):
    """Create a service (dummy route for provider=test)"""
    result = await provider.create_service(service)
    return ServiceResponse(
        id=result.id,
        service_name=result.service_name,
        price=result.price,
        duration=result.duration
    ) 