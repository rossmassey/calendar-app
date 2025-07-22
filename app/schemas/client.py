from typing import List, Optional
from pydantic import BaseModel


class ClientResponse(BaseModel):
    id: str
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class ClientListResponse(BaseModel):
    clients: List[ClientResponse]
    total: int 