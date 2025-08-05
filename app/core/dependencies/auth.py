from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.database.session import get_db  
from app.core.config import settings
from app.models.user import User
from app.repositories.user_repository import get_user_by_email


oauth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="auth/login")
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se encontraron credenciales validas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

def get_current_admin(current_user: User = Depends(get_current_user)):
     if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los administradores pueden acceder a este recurso"
        )
     return current_user

def get_current_doctor(current_user: User = Depends(get_current_user)):
    if current_user.role != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los doctores pueden acceder a este recurso"
        )
    return current_user

def get_current_patient(current_user: User = Depends(get_current_user)):
    if current_user.role != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los pacientes pueden acceder a este recurso"
        )
    return current_user 