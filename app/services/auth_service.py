from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.core.security import create_access_token,verify_password, hash_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user_repository import get_user_by_email, create_user

def register_user(db: Session, user_in: UserCreate):
    if user_in.role != "patient":
        raise HTTPException(status_code=403, detail="Solo se permiten pacientes en el registro.")
    
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya ha sido registrado antes")
    
    hashed_pw = hash_password(user_in.password)
    return create_user(db, user_in, hashed_pw)

def authenticate_user(db: Session, email: EmailStr, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return user

def login_for_access_token(db: Session, email: EmailStr, password: str):
    user = authenticate_user(db, email, password)
    return create_access_token(data={"sub": user.email})

