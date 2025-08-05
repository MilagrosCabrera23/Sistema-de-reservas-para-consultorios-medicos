from pydantic import BaseModel
from  datetime import datetime
from enum import Enum 
from typing import Optional

class AppointmentStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class AppointmentBase(BaseModel):
    title:str 
    patient_id:int
    doctor_id:int
    service_id:int
    date: datetime
    status: AppointmentStatus
    notes: Optional[str]

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    title:Optional[str]
    date: Optional[datetime]
    status: Optional[AppointmentStatus]
    notes: Optional[str]

class Appointment(AppointmentBase):
    id:int 

    class Config:
        from_attributes = True