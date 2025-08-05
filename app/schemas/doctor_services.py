from pydantic import BaseModel

class DoctorServicesBase(BaseModel):
    doctor_id: int
    service_id: int

class DoctorServicesCreate(DoctorServicesBase):
    pass 

class DoctorServices(DoctorServicesBase):

    class Config:
      from_attributes = True