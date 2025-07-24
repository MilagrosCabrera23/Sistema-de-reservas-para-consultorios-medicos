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

class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True

