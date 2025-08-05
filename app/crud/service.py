from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate
from app.repositories.service_repository import get_service_by_id, create_new_service,get_service_by_name, get_all_services, update_service, delete_service
from fastapi import HTTPException

def create_new_service(db: Session, service_in: ServiceCreate):
   existing_service = get_service_by_name(db, service_in.name)
   if existing_service:
       raise HTTPException(status_code=400, detail="El servicio ya ha sido registrado")
   return create_new_service(db, service_in)

def get_all_services(db: Session):
    return get_all_services(db)

def get_service_by_name(db: Session, name: str):
    service = get_service_by_name(db, name)
    if not service:
        raise HTTPException(status_code=404, detail="No se encontro el servicio")
    return service

def get_service_by_id(db: Session, service_id: int):
    db_service = get_service_by_id(db, service_id)
    if not db_service:
        raise HTTPException(status_code=404, detail="No se encontro el servicio")
    return db_service

def update_service(db: Session, service_id: int, service_in: ServiceUpdate):
    service = get_service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="No se encontro el servicio")
    return update_service(db, service, service_in)

def delete_service(db: Session, service_id: int):
   db_service = get_service_by_id(db, service_id)
   if not db_service:
       raise HTTPException(status_code=404, detail="No se encontro el servicio")
   delete_service(db, db_service)
   return {"details": "Servicio eliminado correctamente"}