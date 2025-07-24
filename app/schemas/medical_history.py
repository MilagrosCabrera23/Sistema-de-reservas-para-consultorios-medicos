from pydantic import BaseModel
from typing import Optional

class MedicalHistoryBase(BaseModel):
    allergies: Optional[str] = None
    chronic_conditions: Optional[str] = None
    medications: Optional[str] = None
    surgeries: Optional[str] = None
    family_history: Optional[str] = None
    notes: Optional[str] = None

class MedicalHistoryCreate(MedicalHistoryBase):
    pass

class MedicalHistory(MedicalHistoryBase):
    id:int 
    patient_id:int

    class Config:
        orm_mode = True 