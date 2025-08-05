from fastapi import APIRouter, Depends,HTTPException    
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.patient import Patient, PatientCreate, PatientUpdate
from app.crud.patient import create_new_patient, get_all_patients, get_patient_by_id, update_patient, delete_patient

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=Patient)
async def create_patient_route(
    patient_in: PatientCreate,
    db: Session = Depends(get_db),
   curerent_user = Depends(get_current_user)
    ):
    return create_new_patient(db, patient_in)

@router.get("/", response_model=list[Patient])
async def get_patients_route(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
        return get_all_patients(db)

@router.get("/{patient_id}", response_model=Patient)
async def get_patient_by_id_route(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return get_patient_by_id(db, patient_id)

@router.put("/{patient_id}", response_model=Patient)
async def update_patient_route(
    patient_id: int,
    patient_in: PatientUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    return update_patient(db, patient_id, patient_in)

@router.delete("/{patient_id}")
async def delete_patient_route(
    patient_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    result = delete_patient(db, patient_id)
    return JSONResponse(content = result)