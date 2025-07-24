from pydantic import BaseModel
import datetime
from enum import Enum 
from typing import Optional

class AppointmentStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class AppointmentBase(BaseModel):
    patient_id:int
    doctor_id:int
    service_id:int
    date: datetime
    status: AppointmentStatus
    notes: Optional[str]


class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id:int 

    class Config:
        orm_mode = True