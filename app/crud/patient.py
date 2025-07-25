from sqlalchemy import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate
from fastapi import HTTPException


def create_new_patient(db: Session, patient_in: PatientCreate):
    db_patient = Patient(**patient_in.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_all_patients(db: Session):
    return db.query(Patient).all()

def get_patient_by_id(db: Session, patient_id: int):
    patient =  db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

def update_patient(db: Session, patient_id: int, updated_data: PatientUpdate):
    patient = get_patient_by_id(db, patient_id)
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int, updated_data: PatientUpdate):
    db_patient = get_patient_by_id(db, patient_id)
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(db_patient, key, value)
    db.delete(db_patient)
    db.commit()
     
    delete_patient(db, patient_id)
    return {"detail": "Paciente eliminado correctamente"}
