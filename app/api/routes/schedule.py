from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.schedule import Schedule, ScheduleCreate, ScheduleUpdate  
from app.crud.schedule import create_new_schedule, get_all_schedules, get_schedule_by_id,get_schedule_by_name, update_schedule, delete_schedule


router = APIRouter(prefix="/schedules", tags=["Schedules"])

@router.post("/", response_model=Schedule)
async def create_schedule_route(schedule_in: ScheduleCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_schedule(db, schedule_in)

@router.get("/", response_model=List[Schedule])
async def get_schedules_route(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_all_schedules(db)

@router.get("/{schedule_id}", response_model=Schedule)
async def get_schedule_by_id_route(schedule_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_schedule_by_id(db, schedule_id)

@router.get("/by-name/{name}", response_model=Schedule)
async def get_schedule_by_name_route(name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    schedule = get_schedule_by_name(db, name)
    if not schedule:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return schedule

@router.put("/{schedule_id}", response_model=Schedule)
async def update_schedule_route(schedule_id: int, schedule_in: ScheduleUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_schedule(db, schedule_id, schedule_in)

@router.delete("/{schedule_id}")
async def delete_schedule_route(schedule_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result = delete_schedule(db, schedule_id)
    return JSONResponse(content=result)