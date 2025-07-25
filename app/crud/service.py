from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate

from fastapi import HTTPException

def create_new_service(db: Session, service_in: ServiceCreate):
    db_service = Service(**service_in.model_dump())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def get_all_services(db: Session):
    return db.query(Service).all()

def get_service_by_id(db: Session, service_id: int):
    service =  db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="No se encontro el servicio")
    return service

def update_service(db: Session, service_id: int, service_in: ServiceUpdate):
    db_service = get_service_by_id(db, service_id)
    for key, value in service_in.model_dump(exclude_unset=True).items():
        setattr(db_service, key, value)
    db.commit()
    db.refresh(db_service)
    return db_service

def delete_service(db: Session, service_id: int):
    db_service = get_service_by_id(db, service_id)
    db.delete(db_service)
    db.commit()
    return {"details": "Servicio eliminado correctamente"}