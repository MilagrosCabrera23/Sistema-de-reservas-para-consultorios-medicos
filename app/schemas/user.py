from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    full_name: str  
    email: EmailStr
    address: str
    birth_date: date
    age: int
    phone: str
    role: str = "patient"
    is_active: bool = True 

class UserCreate(UserBase):
    password:str 

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    birth_date: Optional[date] = None
    age: Optional[int] = None
    phone: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id:int
    
    class Config:
       from_attributes = True