from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.client import ClientCreate, ClientUpdate
from app.schemas.client import ClientResponse
from app.providers.test_provider import TestProvider
from app.dependencies import get_provider

router = APIRouter()


@router.post("/", response_model=ClientResponse)
async def create_client(
    client: ClientCreate,
    provider: TestProvider = Depends(get_provider)
):
    """Create a new client"""
    result = await provider.create_client(client)
    return ClientResponse(
        id=result.id,
        name=result.name,
        phone=result.phone,
        email=result.email
    )


@router.get("/{client_id}", response_model=ClientResponse)
async def get_client(
    client_id: str,
    provider: TestProvider = Depends(get_provider)
):
    """Get a client by ID"""
    client = await provider.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return ClientResponse(
        id=client.id,
        name=client.name,
        phone=client.phone,
        email=client.email
    )


@router.get("/", response_model=List[ClientResponse])
async def get_all_clients(
    provider: TestProvider = Depends(get_provider)
):
    """Get all clients"""
    clients = await provider.get_all_clients()
    return [
        ClientResponse(
            id=client.id,
            name=client.name,
            phone=client.phone,
            email=client.email
        )
        for client in clients
    ]


@router.delete("/{client_id}")
async def delete_client(
    client_id: str,
    provider: TestProvider = Depends(get_provider)
):
    """Delete a client"""
    success = await provider.delete_client(client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"} 