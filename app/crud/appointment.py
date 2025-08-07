from sqlalchemy.orm import Session
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate
from app.repositories.appointment_repository import (create_appointment, get_all_appointments,get_appointment_by_id,get_appointments_by_patient_id,get_appointments_by_doctor_id,get_appointments_by_date,get_appointment_by_patient_and_date,update_appointment,delete_appointment)
from app.repositories.doctor_repository import get_doctor_by_id
from app.repositories.patient_repository import get_patient_by_id
from app.repositories.service_repository import get_service_by_id

from fastapi import HTTPException,status

def create_new_appointment_service(db: Session, appointment_in: AppointmentCreate):

     # Validar que el doctor existe
    if not get_doctor_by_id(db, appointment_in.doctor_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor no encontrado.")
    
    # Validar que el paciente existe
    if not get_patient_by_id(db, appointment_in.patient_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado.")
    
    # Validar que el servicio existe
    if not get_service_by_id(db, appointment_in.service_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado.")
    
    # Validar que el doctor no tenga otra cita en el mismo horario
    existing_appointment = get_appointment_by_patient_and_date(db, appointment_in.doctor_id, appointment_in.date)
    if existing_appointment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El doctor ya tiene una cita agendada en ese horario."
        )
    return create_appointment(db, appointment_in)

def get_all_appointment_service(db: Session):
    return get_all_appointments(db)

def get_appointment_by_id_service(db: Session, appointment_id: int):
    return get_appointment_by_id(db, appointment_id)
    
def appointments_by_patient_id_service(db: Session, patient_id: int):
    appointments = get_appointments_by_patient_id(db, patient_id)
    if not appointments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron citas para el paciente proporcionado")
    return appointments

def get_appointments_by_doctor_id_service(db:Session, doctor_id: int):
    appointments = get_appointments_by_doctor_id(db, doctor_id)
    if not appointments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron citas para el doctor proporcionado")
    return appointments

def get_appointments_by_date_service(db: Session, date: str):
    appointments = get_appointments_by_date(db, date)
    if not appointments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron citas para la fecha proporcionada")
    return appointments

def update_appointment_service(db: Session, appointment_id: int,  updated_data: AppointmentUpdate):
    db_appointment = get_appointment_by_id(db, appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La cita no se encontro")
    return update_appointment(db, db_appointment, updated_data)

def delete_appointment_service(db: Session, appointment_id: int):
    db_appointment = get_appointment_by_id(db, appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La cita no se encontro")
    delete_appointment(db, db_appointment)
    return {"detail": "Cita eliminada correctamente"}