from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from typing import List,Optional
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.doctor import Doctor, DoctorCreate,DoctorUpdate
from app.crud.doctor import (create_new_doctor_service, get_all_doctors_service, get_doctor_by_id_service, get_doctor_by_user_id_service,get_doctor_by_specialty_service,get_doctor_by_name_service,get_doctor_by_email_service, update_doctor_service, delete_doctor_service)

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=Doctor,status_code=201) 
async def create_doctor_route(
    doctor_in: DoctorCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):   
    return create_new_doctor_service(db, doctor_in)

@router.get("/", response_model=List[Doctor], status_code=200)
async def get_doctors_route(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_doctors_service(db)

@router.get("/search", response_model=List[Doctor], status_code=200)
async def search_doctors_routes(
    name: Optional[str] = Query(None),
    specialty: Optional[str] = Query(None), 
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if name:
        return get_doctor_by_name_service(db, name)
    elif specialty:
        return get_doctor_by_specialty_service(db, specialty)
    elif email:
        return get_doctor_by_email_service(db, email)
    else:
        return {"details": "Provide name, specialty, or email parameter"}

@router.get("/user/{user_id}", response_model=Doctor,status_code=200 )
async def get_doctor_by_user_id_route(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    return get_doctor_by_user_id_service(db, user_id)

@router.get("/{doctor_id}", response_model=Doctor , status_code=200)
async def get_doctor_by_id_route(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return get_doctor_by_id_service(db, doctor_id)

@router.put("/{doctor_id}", response_model=Doctor,status_code=200)
async def update_doctor_route(
    doctor_id: int,
    doctor_in: DoctorUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    return update_doctor_service(db, doctor_id, doctor_in)

@router.delete("/{doctor_id}", status_code=204)
async def delete_doctor_route(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    result = delete_doctor_service(db, doctor_id)
    return JSONResponse(content=result)