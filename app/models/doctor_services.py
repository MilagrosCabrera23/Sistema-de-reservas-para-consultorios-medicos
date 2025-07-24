from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database.base import Base

ServiceDoctor = Table(
    "doctor_services",
    Base.metadata,
    Column("doctor_id", Integer, ForeignKey("doctors.id"), primary_key=True),
    Column("service_id", Integer, ForeignKey("services.id"), primary_key=True)
)