from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Numbers(BaseModel):
    a:int
    b:int