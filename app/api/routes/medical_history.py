from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.medical_history import MedicalHistory, MedicalHistoryCreate, MedicalHistoryUpdate
from app.crud.medical_history import create_new_medical_history, get_all_medical_histories, get_medical_history_by_id, update_medical_history, delete_medical_history

router = APIRouter(prefix="/medical_history", tags=["Medical History"])

@router.post("/", response_model=MedicalHistory)
async def create_medical_history_route(medical_history_in: MedicalHistoryCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_medical_history(db, medical_history_in)

@router.get("/", response_model=list[MedicalHistory])
async def get_all_medical_historys(db:Session = Depends(get_db), current_user: get_current_admin = Depends(get_current_admin)):
    return get_all_medical_histories(db)

@router.get("/{medical_history_id}", response_model=MedicalHistory)
async def get_medical_history_by_id_route(medical_history_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_medical_history_by_id(db, medical_history_id)

@router.put("/{medical_history_id}", response_model=MedicalHistory)
async def update_medical_history_route(medical_history_id: int, medical_history_in: MedicalHistoryUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_medical_history(db, medical_history_id, medical_history_in)

@router.delete("/{medical_history_id}")
async def delete_medical_history_route(medical_history_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result =  delete_medical_history(db, medical_history_id)
    return JSONResponse(content=result)



