from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    user_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # plain text or hashed before saving
    client_id: int  # link to the company/client

class UserResponse(UserBase):
    user_id: int
    client_id: int
    created_at: datetime

    class Config:
        orm_mode = True
