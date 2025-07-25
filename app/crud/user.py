from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

from fastapi import HTTPException

def create_new_user(db: Session, user_in: UserCreate): 
    db_user = User(**user_in.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db:Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
   user =  db.query(User).filter(User.id == user_id).first()
   if not user:
       raise HTTPException(status_code=404, detail="No se encontro el usuario")
   return user

def update_user(db: Session, user_id: int, updated_data: UserUpdate):
    user = get_user_by_id(db, user_id)
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session, user_id:int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
    return {"details": "Usuario eliminado correctamente"}
