from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate

def create_service(db: Session, service: ServiceCreate) -> Service:
    db_service = Service(**service.model_dump())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def get_all_services(db: Session) -> list[Service]:
    return db.query(Service).all()

def get_service_by_id(db: Session, service_id: int) -> Service | None:
    return db.query(Service).filter(Service.id == service_id).first()

def get_service_by_name(db: Session, name: str) -> Service | None:
    return db.query(Service).filter(Service.name == name).first()

def update_service(db: Session, service: Service, updated_data: ServiceUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(service, key, value)
    db.commit()
    db.refresh(service)
    return service

def delete_service(db: Session, service: Service):
    db.delete(service)
    db.commit()