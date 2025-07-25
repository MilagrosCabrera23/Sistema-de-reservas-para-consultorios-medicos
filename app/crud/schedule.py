from sqlalchemy.orm import  Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate

def create_new_schedule(db:Session, schedule_in: ScheduleCreate):
    db_schedule = Schedule(**schedule_in.model_dump())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_all_schedules(db:Session):
    return db.query(Schedule).all()

def get_schedule_by_id(db:Session, schedule_id:int):
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()

def get_schedule_by_name(db:Session, schedule_name:str):
    return db.query(Schedule).filter(Schedule.name == schedule_name).first()

def update_schedule(db:Session, schedule_id:int, schedule_in:ScheduleUpdate):
    db_schedule = get_schedule_by_id(db, schedule_id)
    for key, value in schedule_in.model_dump(exclude_unset=True).items():
        setattr(db_schedule, key, value)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db:Session, schedule_id:int):
    db_schedule = get_schedule_by_id(db, schedule_id)
    db.delete(db_schedule)
    db.commit()
    return {"details": "Horario eliminado correctamente"}