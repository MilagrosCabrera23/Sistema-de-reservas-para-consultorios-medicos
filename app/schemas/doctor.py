from pydantic import BaseModel
from typing import Optional

class DoctorBase(BaseModel):
    specialty:str
    office:str

class DoctorCreate(DoctorBase):
    user_id:int

class DoctorUpdate(BaseModel): 
    specialty: Optional[str] = None
    office: Optional[str] = None
    
class Doctor(DoctorBase):
    id:int 
    user_id:int

    class Config:
       from_attributes = True