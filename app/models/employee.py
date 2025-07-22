from pydantic import BaseModel
from typing import Optional, List


class EmployeeCreate(BaseModel):
    name: str
    center_id: str
    specialties: List[str] = []
    phone: Optional[str] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    specialties: Optional[List[str]] = None
    phone: Optional[str] = None


class Employee(BaseModel):
    id: str
    name: str
    center_id: str
    specialties: List[str] = []
    phone: Optional[str] = None
    is_available: bool = True
    
    class Config:
        from_attributes = True 