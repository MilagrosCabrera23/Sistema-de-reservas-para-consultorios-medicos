from pydantic import BaseModel

class ScheduleBase(BaseModel):
    doctor_id:int
    day_of_week: str
    start_time: str
    end_time: str
    is_available: bool

class ScheduleCreate(ScheduleBase):
    pass 

class Schedule(ScheduleBase):
      id:int
      
      class Config:
        orm_mode = True