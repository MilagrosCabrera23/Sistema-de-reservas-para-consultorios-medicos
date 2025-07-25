from sqlalchemy import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.service import Service, ServiceCreate, ServiceUpdate
from app.crud.service import create_new_service, get_all_services, get_service_by_id, update_service, delete_service

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=Service)
async def create_service_route(service_in: ServiceCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_service(db, service_in)

@router.get("/", response_model=List[Service])
async def get_services_route(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_all_services(db)

@router.get("/{service_id}", response_model=Service)
async def get_service_by_id_route(service_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_service_by_id(db, service_id)

@router.put("/{service_id}", response_model=Service)
async def update_service_route(service_id: int, service_in: ServiceUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_service(db, service_id, service_in)

@router.delete("/{service_id}", response_model=Service)
async def delete_service_route(service_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return delete_service(db, service_id)