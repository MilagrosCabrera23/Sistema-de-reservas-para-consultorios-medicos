from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate

def create_new_schedule(db: Session, schedule: ScheduleCreate) -> Schedule:
    db_schedule = Schedule(**schedule.model_dump())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def get_all_schedules(db: Session) -> list[Schedule]:
    return db.query(Schedule).all()

def get_schedule_by_id(db: Session, schedule_id: int) -> Schedule | None:
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()

def get_schedule_by_name(db: Session, name: str) -> Schedule | None:
    return db.query(Schedule).filter(Schedule.name == name).first()

def update_schedule(db: Session, schedule: Schedule, updated_data: ScheduleUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(schedule, key, value)
    db.commit()
    db.refresh(schedule)
    return schedule

def delete_schedule(db: Session, schedule: Schedule):
    db.delete(schedule)
    db.commit()