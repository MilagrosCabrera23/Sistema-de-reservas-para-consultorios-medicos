from sqlalchemy.orm import Session
from app.models.user import User
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate

def create_doctor(db: Session, doctor_in: DoctorCreate) -> Doctor:
    doctor = Doctor(**doctor_in.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_all_doctors(db: Session) -> list[Doctor]:
    return db.query(Doctor).all()

def get_doctor_by_id(db: Session, doctor_id: int) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_doctor_by_user_id(db: Session, user_id: int) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.user_id == user_id).first()

def get_doctor_by_specialty(db: Session, specialty: str) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.specialty == specialty).first()

def get_doctor_by_name(db: Session, name: str) -> Doctor | None:
    return db.query(Doctor).join(User).filter(User.full_name== name).first()

def get_doctor_by_email(db: Session, email: str) -> Doctor | None:
    return db.query(Doctor).join(User).filter(User.email == email).first()

def update_doctor(db: Session, doctor: Doctor, updated_data: DoctorUpdate) -> Doctor:
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(doctor, key, value)
    db.commit()
    db.refresh(doctor)
    return doctor

def delete_doctor(db: Session, doctor: Doctor):
    db.delete(doctor)
    db.commit()