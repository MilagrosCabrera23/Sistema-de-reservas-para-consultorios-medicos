from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.doctor import Doctor, DoctorCreate,DoctorUpdate
from app.crud.doctor import create_new_doctor, get_all_doctors, get_doctor_by_id, update_doctor, delete_doctor

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=Doctor) 
async def create_doctor_route(
    doctor_in: DoctorCreate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    return create_new_doctor(db, doctor_in)

@router.get("/", response_model=List[Doctor])
async def get_doctors_route(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_doctors(db)

@router.get("/{doctor_id}", response_model=Doctor)
async def get_doctor_by_id_route(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    return get_doctor_by_id(db, doctor_id)


@router.put("/{doctor_id}", response_model=Doctor)
async def update_doctor_route(
    doctor_id: int,
    doctor_in: DoctorUpdate,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
    ):
    return update_doctor(db, doctor_id, doctor_in)

@router.delete("/{doctor_id}", response_model=Doctor)
async def delete_doctor_route(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin)
):
    result = delete_doctor(db, doctor_id)
    return JSONResponse(content=result)