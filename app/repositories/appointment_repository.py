from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate

def create_appointment(db: Session, appointment_in: AppointmentCreate) -> Appointment:
    appointment = Appointment(**appointment_in.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_all_appointments(db: Session) -> list[Appointment]:
    return db.query(Appointment).all()

def get_appointment_by_id(db: Session, appointment_id: int) -> Appointment | None:
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def get_appointments_by_patient_id(db: Session, patient_id: int) -> list[Appointment]:
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

def get_appointments_by_doctor_id(db: Session, doctor_id: int) -> list[Appointment]:
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

def get_appointments_by_date(db: Session, appointment_date: date) -> list[Appointment]:
    return db.query(Appointment).filter(Appointment.date == appointment_date).all()

def get_appointment_by_patient_and_date(db: Session, patient_id: int, appointment_date: date) -> Appointment | None:
    return db.query(Appointment).filter(
        Appointment.patient_id == patient_id,
        Appointment.date == appointment_date
    ).first()

def update_appointment(db: Session, appointment: Appointment, updated_data: AppointmentUpdate) -> Appointment:
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(appointment, key, value)
    db.commit()
    db.refresh(appointment)
    return appointment

def delete_appointment(db: Session, appointment: Appointment):
    db.delete(appointment)
    db.commit()