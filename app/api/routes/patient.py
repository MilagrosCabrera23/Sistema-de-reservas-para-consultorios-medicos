from fastapi import APIRouter, Depends,HTTPException    
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.patient import Patient, PatientCreate, PatientUpdate
from app.crud.patient import create_new_patient_service, get_all_patients_service, get_patient_by_user_id_service, get_patient_by_id_service, get_patient_by_name_service,update_patient_service, delete_patient_service

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=Patient,status_code=201)
async def create_patient_route(
    patient_in: PatientCreate,
    db: Session = Depends(get_db),
   current_user = Depends(get_current_user)
    ):
    return create_new_patient_service(db, patient_in)

@router.get("/", response_model=list[Patient],status_code=200)
async def get_patients_route(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
        return get_all_patients_service(db)

@router.get("/user/{user_id}", response_model=Patient,status_code=200)
async def get_patient_by_user_id_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_patient_by_user_id_service(db, user_id)

@router.get("/{patient_id}", response_model=Patient,status_code=200)
async def get_patient_by_id_route(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return get_patient_by_id_service(db, patient_id)

@router.get("/name/{name}", response_model=Patient,status_code=200)
async def get_patient_by_name_route(
    name: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return get_patient_by_name_service(db, name)

@router.put("/{patient_id}", response_model=Patient,status_code=200)
async def update_patient_route(
    patient_id: int,
    patient_in: PatientUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    return update_patient_service(db, patient_id, patient_in)

@router.delete("/{patient_id}",status_code=204)
async def delete_patient_route(
    patient_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    result = delete_patient_service(db, patient_id)
    return JSONResponse(content = result)