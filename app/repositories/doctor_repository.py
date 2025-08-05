from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate

def create_new_doctor(db: Session, doctor_in: DoctorCreate) -> Doctor: