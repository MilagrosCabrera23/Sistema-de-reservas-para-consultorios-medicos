from sqlalchemy.orm import Session
from app.models.medical_history import Medical
from app.schemas.medical_history import MedicalCreate, MedicalUpdate

def create_new_medical(db: Session, medical_in: MedicalCreate):
    db_medical = Medical(**medical_in.model_dump())
    db.add(db_medical)
    db.commit()
    db.refresh(db_medical)
    return db_medical

def get_all_medicals(db: Session) -> list[Medical]:
    return db.query(Medical).all()

def get_medical_by_id(db: Session, medical_id: int) -> Medical | None:
    return db.query(Medical).filter(Medical.id == medical_id).first()

def get_medical_by_name(db: Session, name: str) -> Medical | None:
    return db.query(Medical).filter(Medical.name == name).first()

def update_medical(db: Session, medical: Medical, updated_data: MedicalUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(medical, key, value)
    db.commit()
    db.refresh(medical)
    return medical

def delete_medical(db: Session, medical: Medical):
    db.delete(medical)
    db.commit()