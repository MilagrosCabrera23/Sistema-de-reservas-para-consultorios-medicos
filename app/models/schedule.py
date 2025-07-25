from sqlalchemy import Column, Integer, ForeignKey, Time, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database.base import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), nullable=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    day_of_week = Column(String(10))  # "Monday", "Tuesday", etc.
    start_time = Column(Time)
    end_time = Column(Time)
    is_available = Column(Boolean, default=True)

    doctor = relationship("Doctor", backref="schedules")