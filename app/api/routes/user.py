from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin, get_current_user
from app.schemas.user import User, UserCreate, UserUpdate
from app.crud.user import (
    create_new_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
async def create_user_route(user_in: UserCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_new_user(db, user_in)

@router.get("/", response_model=List[User])
async def get_users_route(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=User)
async def get_user_route(user_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=User)
async def update_user_route(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_user(db, user_id, user_in)

@router.delete("/{user_id}")
async def delete_user_route(user_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result = delete_user(db, user_id)
    return JSONResponse(content = result)