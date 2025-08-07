from sqlalchemy.orm import  Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from app.repositories.schedule_repository import (
    create_schedule,
    get_schedule_by_id,
    get_schedule_by_name,
    update_schedule,
    get_all_schedules,
    delete_schedule
)
from fastapi import HTTPException,status

def create_schedule_service(db:Session, schedule_in: ScheduleCreate):
    existing_schedule = get_schedule_by_name(db, schedule_in.name)
    if existing_schedule:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El horario ya ha sido registrado")
    return create_schedule(db, schedule_in)

def get_all_schedules_service(db:Session):
    return get_all_schedules(db)

def get_schedule_by_id_service(db:Session, schedule_id:int):
    db_schedule = get_schedule_by_id(db, schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el horario")
    return db_schedule

def get_schedule_by_name_service(db:Session, schedule_name:str):
   db_schedule = get_schedule_by_name(db, schedule_name)
   if not db_schedule:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el horario")
   return db_schedule

def update_schedule_service(db:Session, schedule_id:int, schedule_in:ScheduleUpdate):
    db_schedule = get_schedule_by_id(db, schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el horario")
    return update_schedule(db, db_schedule, schedule_in)

def delete_schedule_service(db:Session, schedule_id:int):
    db_schedule = get_schedule_by_id(db, schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el horario")
    delete_schedule(db, db_schedule)
    return {"details": "Horario eliminado correctamente"}