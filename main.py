from fastapi import FastAPI
from app.core.database.connection import engine
from app.core.database.base import Base
from app.api.routes import api_route
from app.api.routes import auth

app = FastAPI(
    title="Sistema de reservas para consultorios medicos",
    description="El sistema de Reservas sirve para gestionar las reservas de turnos médicos entre pacientes y profesionales de la salud, con un sistema de autenticación seguro y una arquitectura modular escalable.",)

Base.metadata.create_all(bind=engine)

app.include_router(api_route)
app.include_router(auth.router)