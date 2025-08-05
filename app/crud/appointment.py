from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.service import Service
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

from fastapi import HTTPException

def create_new_appointment(db: Session, appointment: AppointmentCreate):
    existing_appointment = db.query(Appointment).filter(
        Appointment.doctor_id == appointment.doctor_id,
        Appointment.date == appointment.date
    ).first()

    if existing_appointment:
        raise HTTPException(
            status_code=400,
            detail="El doctor ya tiene una cita agendada en ese horario."
        )

    if not db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first():
        raise HTTPException(status_code=404, detail="Doctor no encontrado.")

   
    if not db.query(Patient).filter(Patient.id == appointment.patient_id).first():
        raise HTTPException(status_code=404, detail="Paciente no encontrado.")

   
    if not db.query(Service).filter(Service.id == appointment.service_id).first():
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")

    db_appointment = Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_all_appointment(db: Session):
    return db.query(Appointment).all()

def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def get_appointments_by_title(db: Session, title: str):
    return db.query(Appointment).filter(Appointment.title == title).all()

def update_appointment(db: Session, appointment_id: int, appointment: AppointmentUpdate):
    db_appointment = get_appointment_by_id(db, appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="La cita no se encontro")
    for key, value in appointment.model_dump().items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = get_appointment_by_id(db, appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="La cita no se encontro")
    db.delete(db_appointment)
    db.commit()
    return {"detail": "Cita eliminada correctamente" }