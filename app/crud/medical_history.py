from sqlalchemy.orm import Session
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate, MedicalHistoryUpdate
from app.repositories.medical_repository import (
    get_medical_by_id,
    create_new_medical,
    update_medical,
    get_all_medicals,
    delete_medical
)
from fastapi import HTTPException

def create_new_medical_history(db: Session, medical_history_in: MedicalHistoryCreate):
    db_medical_history = get_medical_by_id(db, medical_history_in.patient_id)   
    if db_medical_history:
        raise HTTPException(status_code=400, detail="La historia medica ya ha sido registrada")
    return create_new_medical_history(db, medical_history_in)

def get_all_medical_histories(db: Session):
    return get_all_medical_histories(db) 

def get_medical_history_by_id(db: Session, medical_history_id: int):
    medical_history =  get_medical_history_by_id(db, medical_history_id)
    if not medical_history:
        raise HTTPException(status_code=404, detail="La historia medica no fue encontrada")
    return medical_history

def update_medical_history(db:Session, medical_history_id: int, updated_data: MedicalHistoryUpdate):
    medical_history = get_medical_history_by_id(db, medical_history_id)
    if not medical_history:
        raise HTTPException(status_code=404, detail="La historia medica no fue encontrada")
    return update_medical_history(db, medical_history, updated_data)

def delete_medical_history(db: Session, medical_history_id: int):
    db_medical_history = get_medical_history_by_id(db, medical_history_id)
    if not db_medical_history:
        raise HTTPException(status_code=404, detail="La historia medica no fue encontrada")
    delete_medical_history(db, db_medical_history)
    return {"details": "Historia medica eliminada correctamente"}