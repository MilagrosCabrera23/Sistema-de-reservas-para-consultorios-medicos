from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.models.user import User 
from app.models.medical_history import Medical
from app.schemas.medical_history import MedicalCreate, MedicalUpdate


def create_medical_history(db: Session, medical_in: MedicalCreate):
    db_medical = Medical(**medical_in.model_dump())
    db.add(db_medical)
    db.commit()
    db.refresh(db_medical)
    return db_medical

def get_all_medicals(db: Session) -> list[Medical]:
    return db.query(Medical).all()

def get_medical_by_id(db: Session, medical_id: int) -> Medical | None:
    return db.query(Medical).filter(Medical.id == medical_id).first()

def get_medical_by_patient_id(db: Session, patient_id: int) -> list[Medical]:
    return db.query(Medical).filter(Medical.patient_id == patient_id).all()

def get_medical_histories_by_patient_name(db: Session, patient_name: str) -> list[Medical]:
    return db.query(Medical).join(Patient).join(User).filter(User.full_name == patient_name).all()

def update_medical(db: Session, medical: Medical, updated_data: MedicalUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(medical, key, value)
    db.commit()
    db.refresh(medical)
    return medical

def delete_medical(db: Session, medical: Medical):
    db.delete(medical)
    db.commit()