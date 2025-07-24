from pydantic import BaseModel, EmailStr
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

class User(UserBase):
    id:int
    
    class Config:
        orm_mode = True