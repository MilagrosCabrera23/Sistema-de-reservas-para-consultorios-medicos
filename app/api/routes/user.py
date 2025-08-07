from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse

from app.core.database.session import get_db
from app.core.dependencies.auth import get_current_admin
from app.schemas.user import User, UserCreate, UserUpdate
from app.crud.user import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=201)
async def create_user_route(user_in: UserCreate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return create_user_service(db, user_in)

@router.get("/", response_model=List[User], status_code=200,)
async def get_users_route(db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_all_users_service(db)

@router.get("/{user_id}", response_model=User, status_code=200)
async def get_user_route(user_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return get_user_by_id_service(db, user_id)

@router.put("/{user_id}", response_model=User, status_code=200)
async def update_user_route(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    return update_user_service(db, user_id, user_in)

@router.delete("/{user_id}", status_code=204)
async def delete_user_route(user_id: int, db: Session = Depends(get_db), current_admin = Depends(get_current_admin)):
    result = delete_user_service(db, user_id)
    return JSONResponse(content = result)