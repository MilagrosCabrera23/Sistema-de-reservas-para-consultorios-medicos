from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate
from fastapi import HTTPException

def create_new_doctor(db: Session, doctor_in: DoctorCreate):
    db_doctor = Doctor(**doctor_in.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_all_doctors(db: Session):
     return db.query(Doctor).all()

def get_doctor_by_id(db: Session, doctor_id: int):
   doctor =  db.query(Doctor).filter(Doctor.id == doctor_id).first()
   if not doctor:
       raise HTTPException(status_code=404, detail="Doctor not found")
   return doctor

def update_doctor(db: Session, doctor_id: int, updated_data: DoctorCreate):
  doctor = get_doctor_by_id(db, doctor_id)
  for key, value in updated_data.model_dump().items():
        setattr(doctor, key, value)
  db.commit()
  db.refresh(doctor)
  return doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor_by_id(db, doctor_id)
    db.delete(db_doctor)
    db.commit()
    return 