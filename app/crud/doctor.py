from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate
from app.repositories.doctor_repository import (
    create_doctor,get_all_doctors,get_doctor_by_id, 
    get_doctor_by_user_id, get_doctor_by_specialty,
    get_doctor_by_name, get_doctor_by_email, update_doctor, delete_doctor
)
from fastapi import HTTPException, status

def create_new_doctor_service(db: Session, doctor_in: DoctorCreate):
    db_doctor = get_doctor_by_user_id(db, doctor_in.user_id)
    if db_doctor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El doctor ya existe")
    return create_doctor(db, doctor_in)

def get_all_doctors_service(db: Session):
     return get_all_doctors(db)

def get_doctor_by_id_service(db: Session, doctor_id: int):
   doctor =  get_doctor_by_id(db, doctor_id)
   if not doctor:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor")
   return doctor

def get_doctor_by_user_id_service(db: Session, user_id: int):
    doctor = get_doctor_by_user_id(db, user_id)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor para el usuario proporcionado")
    return doctor

def get_doctor_by_specialty_service(db: Session, specialty: str):
    doctor = get_doctor_by_specialty(db, specialty)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor para la especialidad proporcionada")
    return doctor

def get_doctor_by_name_service(db: Session, name: str):
    doctor = get_doctor_by_name(db, name)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor para el nombre proporcionado")
    return doctor

def get_doctor_by_email_service(db: Session, email: str):
    doctor = get_doctor_by_email(db, email)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor para el correo electronico proporcionado")
    return doctor

def update_doctor_service(db: Session, doctor_id: int, updated_data: DoctorUpdate):
  doctor = get_doctor_by_id(db, doctor_id)
  if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor")
  return update_doctor(db, doctor, updated_data)

def delete_doctor_service(db: Session, doctor_id: int):
    db_doctor = get_doctor_by_id(db, doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el doctor")
    delete_doctor(db, db_doctor)
    return {"details": "El doctor ha sido eliminado correctamente"}