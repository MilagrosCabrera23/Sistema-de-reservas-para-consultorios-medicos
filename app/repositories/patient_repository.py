from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

def create_new_patient(db: Session, patient_in: PatientCreate) -> Patient:
    db_patient = Patient(**patient_in.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_all_patients(db: Session) -> list[Patient]:
    return db.query(Patient).all()

def get_patient_by_id(db: Session, patient_id: int) -> Patient | None:
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_patient_by_name(db: Session, name: str) -> Patient | None:
    return db.query(Patient).filter(Patient.name == name).first()

def update_patient(db: Session, patient: Patient, updated_data: PatientUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient: Patient):
    db.delete(patient)
    db.commit()