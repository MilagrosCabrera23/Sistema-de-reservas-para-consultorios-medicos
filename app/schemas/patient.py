from pydantic import BaseModel

class PatientBase(BaseModel):
    user_id:int

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    user_id:int
    
class Patient(PatientBase):
      id:int

      class Config:
        orm_mode = True
