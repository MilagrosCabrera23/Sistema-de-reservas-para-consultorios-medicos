from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database.base import Base

class Service(Base): 
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    reason = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    duration = Column(Integer, nullable=False)

    appointments = relationship("Appointment", backref="service")
    doctors = relationship("Doctor", secondary="doctor_services", back_populates="services")
