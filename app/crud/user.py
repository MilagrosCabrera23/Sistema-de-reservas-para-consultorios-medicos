from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user_repository import get_user_by_email, create_user,get_all_users, get_user_by_id, update_user, delete_user
from app.core.security import hash_password
from fastapi import HTTPException

def create_new_user(db: Session, user_in: UserCreate): 
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya ha sido registrado")
    
    hashed_password = hash_password(user_in.password)
    return create_user(db, user_in, hashed_password)

def get_all_users(db: Session):
    return get_all_users(db)

def get_user_by_id(db: Session, user_id: int):
   user = get_user_by_id(db, user_id)
   if not user:
       raise HTTPException(status_code=404, detail="No se encontro el usuario")
   return user

def update_user(db: Session, user_id: int, updated_data: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No se encontro el usuario")
    return update_user(db, user, updated_data)

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No se encontro el usuario")
    delete_user(db, user)
    return {"details": "Usuario eliminado correctamente"}
