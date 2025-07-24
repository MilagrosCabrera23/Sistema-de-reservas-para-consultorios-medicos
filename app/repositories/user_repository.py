from sqlalchemy.orm import Session
from app.models.user import User
from pydantic import EmailStr
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email:EmailStr):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in: UserCreate, hashed_password: str):
    db_user = User(
        full_name=user_in.full_name,
        email=user_in.email,
        address=user_in.address,    
        birth_date=user_in.birth_date,
        age=user_in.age,
        phone=user_in.phone,
        role=user_in.role,
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

