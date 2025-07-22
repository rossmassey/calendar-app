from pydantic import BaseModel


class CenterBase(BaseModel):
    center_name: str
    zip_code: str
    time_zone: str


class CenterCreate(CenterBase):
    pass


class CenterUpdate(CenterBase):
    pass


class Center(CenterBase):
    id: str
    
    class Config:
        from_attributes = True 