from pydantic import BaseModel
from typing import Optional

class ServiceBase(BaseModel):
    name: str
    reason: str
    price: float
    description:Optional[str] = None
    duration: int

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    reason: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    duration: Optional[int] = None

class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True

