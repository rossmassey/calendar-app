from pydantic import BaseModel
from typing import Optional, List


class EmployeeCreate(BaseModel):
    """Simple employee creation for AI assistant - providers map this to their complex structures"""
    name: str
    center_id: str
    specialties: List[str] = []
    phone: Optional[str] = None


class EmployeeUpdate(BaseModel):
    """Simple employee update for AI assistant"""
    name: Optional[str] = None
    specialties: Optional[List[str]] = None
    phone: Optional[str] = None


class Employee(BaseModel):
    """Simple employee response for AI assistant"""
    id: str
    name: str
    center_id: str
    specialties: List[str] = []
    phone: Optional[str] = None
    is_available: bool = True
    
    class Config:
        from_attributes = True 