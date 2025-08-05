from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate
from app.repositories.patient_repository import (
    get_patient_by_id,
    create_new_patient,
    update_patient,
    get_all_patients,
    get_patient_by_name,
    delete_patient) 
from fastapi import HTTPException

def create_new_patient(db: Session, patient_in: PatientCreate):
    existing_patient = get_patient_by_name(db, patient_in.name)
    if existing_patient:
        raise HTTPException(status_code=400, detail="El paciente ya ha sido registrado")
    return create_new_patient(db, patient_in)

def get_all_patients(db: Session):
    return get_all_patients(db)

def get_patient_by_id(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

def get_patient_by_name(db: Session, patient_name: str):
    patient = get_patient_by_name(db, patient_name)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

def update_patient(db: Session, patient_id: int, updated_data: PatientUpdate):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return update_patient(db, patient, updated_data)
    
def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient_by_id(db, patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    delete_patient(db, db_patient)
    return {"detail": "Paciente eliminado correctamente"}
