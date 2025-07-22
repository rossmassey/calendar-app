from typing import List
from pydantic import BaseModel


class EmployeeResponse(BaseModel):
    id: str
    center_name: str
    zip_code: str
    time_zone: str


class EmployeeListResponse(BaseModel):
    employees: List[EmployeeResponse]
    total: int 