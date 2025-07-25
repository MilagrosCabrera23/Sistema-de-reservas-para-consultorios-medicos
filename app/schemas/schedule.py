from pydantic import BaseModel
from typing import Optional
from datetime import time

class ScheduleBase(BaseModel):
    name:str
    doctor_id:int
    day_of_week: str
    start_time: time
    end_time: time
    is_available: bool

class ScheduleCreate(ScheduleBase):
    pass 

class ScheduleUpdate(BaseModel):
    name:Optional[str] = None
    doctor_id:Optional[int] = None
    day_of_week:Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    is_available:Optional[bool] = None
    
class Schedule(ScheduleBase):
      id:int
      
      class Config:
        orm_mode = True