from sqlalchemy.orm import Session
from app.models.patient import Patient

from app.schemas.patient import PatientCreate, PatientUpdate
from app.repositories.patient_repository import (
    get_patient_by_id,
    create_patient,
    update_patient,
    get_all_patients,
    get_patient_by_name,
    get_patient_by_email,
    get_patient_by_user_id,
    delete_patient) 
from fastapi import HTTPException, status

def create_new_patient_service(db: Session, patient_in: PatientCreate):
    existing_patient = get_patient_by_user_id(db, patient_in.user_id)
    if existing_patient:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El paciente ya ha sido registrado")
    return create_patient(db, patient_in)

def get_all_patients_service(db: Session):
    return get_all_patients(db)

def get_patient_by_user_id_service(db: Session, user_id: int):
    patient = get_patient_by_user_id(db, user_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el paciente")
    return patient

def get_patient_by_id_service(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el paciente")
    return patient

def get_patient_by_name_service(db: Session, name: str):
    patient = get_patient_by_name(db, name)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el paciente")
    return patient

def update_patient_service(db: Session, patient_id: int, updated_data: PatientUpdate):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el paciente")
    return update_patient(db, patient, updated_data)
    
def delete_patient_service(db: Session, patient_id: int):
    db_patient = get_patient_by_id(db, patient_id)
    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el paciente")
    delete_patient(db, db_patient)
    return {"detail": "Paciente eliminado correctamente"}
