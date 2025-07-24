from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.service import Service
from app.models.schedule import Schedule
from app.models.appointment import Appointment
from app.models.medical_history import MedicalHistory
from app.models.doctor_services import ServiceDoctor