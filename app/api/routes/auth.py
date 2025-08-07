from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.schemas.token import Token
from app.services.auth_service import register_user, login_for_access_token
from app.core.database.session import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=Token,status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = register_user(db, user_in)
    token = login_for_access_token(db, user.email, user_in.password)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=Token, status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = login_for_access_token(db, form_data.username, form_data.password)  
    return {"access_token": token, "token_type": "bearer"}