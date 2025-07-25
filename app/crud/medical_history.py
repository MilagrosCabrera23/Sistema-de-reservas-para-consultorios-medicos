from sqlalchemy import Session
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate, MedicalHistoryUpdate

from fastapi import HTTPException

def create_new_medical_history(db: Session, medical_history_in: MedicalHistoryCreate):
    db_medical_history = MedicalHistory(**medical_history_in.model_dump())
    db.add(db_medical_history)
    db.commit()
    db.refresh(db_medical_history)
    return db_medical_history

def get_all_medical_histories(db: Session):
    return db.query(MedicalHistory).all()

def get_medical_history_by_id(db: Session, medical_history_id: int):
    medical_history =  db.query(MedicalHistory).filter(MedicalHistory.id == medical_history_id).first()
    if not medical_history:
        raise HTTPException(status_code=404, detail="La historia medica no fue encontrada")
    return medical_history

def update_medical_history(db:Session, medical_history_id: int, updated_data: MedicalHistoryUpdate):
    medical_history = get_medical_history_by_id(db, medical_history_id)
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(medical_history, key, value)
    db.commit()
    db.refresh(medical_history)
    return medical_history

def delete_medical_history(db: Session, medical_history_id: int):
    db_medical_history = get_medical_history_by_id(db, medical_history_id)
    db.delete(db_medical_history)
    db.commit()
    return {"details": "Historia medica eliminada correctamente"}