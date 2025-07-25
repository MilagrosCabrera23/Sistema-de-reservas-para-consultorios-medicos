from pydantic import BaseModel
from typing import Optional

class MedicalHistoryBase(BaseModel):
    allergies: str
    chronic_conditions: str
    medications: str
    surgeries: str
    family_history: str
    notes: str

class MedicalHistoryCreate(MedicalHistoryBase):
    pass

class MedicalHistoryUpdate(BaseModel):
    allergies: Optional[str] = None
    chronic_conditions: Optional[str] = None
    medications: Optional[str] = None
    surgeries: Optional[str] = None
    family_history: Optional[str] = None
    notes: Optional[str] = None

class MedicalHistory(MedicalHistoryBase):
    id:int 
    patient_id:int

    class Config:
        orm_mode = True 