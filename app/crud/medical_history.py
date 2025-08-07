from sqlalchemy.orm import Session
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate, MedicalHistoryUpdate
from app.repositories.medical_repository import (
    get_medical_by_id,
    create_medical_history,
    update_medical,
    get_all_medicals,
    get_medical_by_patient_id,
    get_medical_histories_by_patient_name,
    delete_medical
)
from fastapi import HTTPException, status

def create_new_medical_history_service(db: Session, medical_history_in: MedicalHistoryCreate):
    db_medical_history = get_medical_by_id(db, medical_history_in.patient_id)   
    if db_medical_history:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La historia medica ya ha sido registrada")
    return create_medical_history(db, medical_history_in)

def get_all_medical_histories_service(db: Session):
    return get_all_medicals(db)

def get_medical_history_by_id_service(db: Session, medical_history_id: int):
    medical_history =  get_medical_by_id(db, medical_history_id)
    if not medical_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La historia medica no fue encontrada")
    return medical_history

def get_medical_history_by_patient_id_service(db: Session, patient_id: int):
    medical_history = get_medical_by_patient_id(db, patient_id)
    if not medical_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la historia medica del paciente")
    return medical_history

def get_medical_histories_by_patient_name_service(db: Session, patient_name: str):
    medical_histories = get_medical_histories_by_patient_name(db, patient_name)
    if not medical_histories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron historias medicas para el paciente")
    return medical_histories

def update_medical_history_service(db:Session, medical_history_id: int, updated_data: MedicalHistoryUpdate):
    medical_history = get_medical_by_id(db, medical_history_id)
    if not medical_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La historia medica no fue encontrada")
    return update_medical(db, medical_history, updated_data)

def delete_medical_history_service(db: Session, medical_history_id: int):
    db_medical_history = get_medical_by_id(db, medical_history_id)
    if not db_medical_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La historia medica no fue encontrada")
    delete_medical(db, db_medical_history)
    return {"details": "Historia medica eliminada correctamente"}