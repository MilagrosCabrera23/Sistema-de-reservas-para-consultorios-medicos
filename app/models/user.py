from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    address = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String(20), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False) 
    is_active = Column(Boolean, default=True)

    patient = relationship("Patient", back_populates="user", uselist=False)
    doctor = relationship("Doctor", back_populates="user", uselist=False)
    appointments = relationship("Appointment", back_populates="user")
    medical_history = relationship("MedicalHistory", back_populates="user")

