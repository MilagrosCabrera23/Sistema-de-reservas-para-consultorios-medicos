from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.schedule import Schedule, ScheduleCreate, ScheduleUpdate  
from app.crud.schedule import create_schedule_service, get_all_schedules_service, get_schedule_by_id_service,get_schedule_by_name_service, update_schedule_service, delete_schedule_service


router = APIRouter(prefix="/schedules", tags=["Schedules"])

@router.post("/", response_model=Schedule,status_code=201)
async def create_schedule_route(schedule_in: ScheduleCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_schedule_service(db, schedule_in)

@router.get("/", response_model=List[Schedule],status_code=200)
async def get_schedules_route(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_all_schedules_service(db)

@router.get("/{schedule_id}", response_model=Schedule,status_code=200)
async def get_schedule_by_id_route(schedule_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_schedule_by_id_service(db, schedule_id)

@router.get("/by-name/{name}", response_model=Schedule,status_code=200)
async def get_schedule_by_name_route(name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_schedule_by_name_service(db, name)

@router.put("/{schedule_id}", response_model=Schedule,status_code=200)
async def update_schedule_route(schedule_id: int, schedule_in: ScheduleUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_schedule_service(db, schedule_id, schedule_in)

@router.delete("/{schedule_id}", status_code=204)
async def delete_schedule_route(schedule_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result = delete_schedule_service(db, schedule_id)
    return JSONResponse(content=result)