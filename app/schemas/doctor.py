from pydantic import BaseModel

class DoctorBase(BaseModel):
    specialty:str
    office:str

class DoctorCreate(DoctorBase):
    user_id:int

class Doctor(DoctorBase):
    id:int 
    user_id:int

    class Config:
        orm_mode = True