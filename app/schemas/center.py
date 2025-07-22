from typing import List
from pydantic import BaseModel


class CenterResponse(BaseModel):
    id: str
    center_name: str
    zip_code: str
    time_zone: str


class CenterListResponse(BaseModel):
    centers: List[CenterResponse]
    total: int 