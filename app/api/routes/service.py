from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.service import Service, ServiceCreate, ServiceUpdate
from app.crud.service import (create_new_service_service, get_all_services_service,  
get_service_by_name_service,get_service_by_id_service,update_service_service, delete_service_service)

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=Service, status_code=201)
async def create_service_route(service_in: ServiceCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_service_service(db, service_in)

@router.get("/", response_model=List[Service], status_code=200)
async def get_services_route(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_all_services_service(db)

@router.get("/name/{service_name}", response_model=Service,status_code=200)
async def get_service_by_name_route(service_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_service_by_name_service(db, service_name)

@router.get("/{service_id}", response_model=Service, status_code=200)
async def get_service_by_id_route(service_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_service_by_id_service(db, service_id)

@router.put("/{service_id}", response_model=Service,status_code=200)
async def update_service_route(service_id: int, service_in: ServiceUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_service_service(db, service_id, service_in)

@router.delete("/{service_id}", status_code=204)
async def delete_service_route(service_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result =  delete_service_service(db, service_id)
    return JSONResponse(content=result)