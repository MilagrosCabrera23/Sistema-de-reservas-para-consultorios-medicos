from sqlalchemy.orm import Session
from app.models.user import User
from pydantic import EmailStr
from app.schemas.user import UserCreate, UserUpdate

def create_user(db: Session, user_in: UserCreate, hashed_password: str):
    db_user = User(
      **user_in.model_dump(exclude={"password"}),  hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_user_by_email(db: Session, email:EmailStr):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user: User, updated_data: UserUpdate):
    for key, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()