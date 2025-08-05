from fastapi import APIRouter, Depends, Query,HTTPException   
from typing import List
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.crud.appointment import create_new_appointment, get_all_appointment, get_appointment_by_id,get_appointments_by_title, update_appointment, delete_appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/", response_model=Appointment, status_code=201)
async def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_appointment(db, appointment=appointment)

@router.get("/", response_model=List[Appointment])
async def get_all_appointments(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_all_appointment(db)

@router.get("/{appointment_id}", response_model=Appointment)
async def get_appointment_by_id(appointment_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_appointment_by_id(db, appointment_id)

@router.get("/by-title/", response_model=list[Appointment])
def get_appointments_by_title_route(
    title: str = Query(..., description="Título de la cita a buscar"),
    db: Session = Depends(get_db)
):
    results = get_appointments_by_title(db, title)
    if not results:
        raise HTTPException(status_code=404, detail="No se encontraron citas con ese título")
    return results

@router.put("/{appointment_id}", response_model=Appointment)
async def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_appointment(db, appointment_id, appointment)

@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result = delete_appointment(db, appointment_id)
    return JSONResponse(content=result)