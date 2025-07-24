from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
from app.core.database.base import Base

class Patient(Base): 
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", backref="patient")
    medical_history = relationship("MedicalHistory", uselist=False, backref="patient")