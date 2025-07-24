from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database.base import Base

class Doctor(Base): 
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    specialty = Column(String(100), nullable=False)
    office = Column(String(50), nullable=True)

    user = relationship("User", backref="doctor")
    services = relationship("Service", secondary="doctor_services", back_populates="doctors")
  