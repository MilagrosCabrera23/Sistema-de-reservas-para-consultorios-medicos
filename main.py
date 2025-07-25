from fastapi import FastAPI
from app.core.database.connection import engine
from app.core.database.base import Base
from app.api.routes import auth, doctor, patient, service, appointment, schedule, medical_history,user


app = FastAPI(
    title="Sistema de reservas para consultorios medicos",
    description="El sistema de Reservas sirve para gestionar las reservas de turnos médicos entre pacientes y profesionales de la salud, con un sistema de autenticación seguro y una arquitectura modular escalable.",)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(service.router)
app.include_router(schedule.router)
app.incluide_router(medical_history.router)

app.include_router(appointment.router)