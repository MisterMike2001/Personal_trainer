from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserBase (BaseModel):
    name:str
    surname:str
    email:str
    cell:str

class UserCreate(UserBase):
    password:str
    is_admin:bool = Field(default=False)

class UserUpdate(BaseModel):
    name:str
    surname:str
    email:str
    is_admin:bool = Field(default=False)
    cell:str

class UserLogin(BaseModel):
    email:str
    password:str

class UserPasswordChange(BaseModel):
    old_password:str
    new_password:str

class UserResponse(UserBase):
    id:int
    is_admin:bool
    create_dt:datetime

    model_config = ConfigDict(from_attributes=True)



class RefreshRequest(BaseModel):
    refresh_token: str = Field(min_length=1)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = 900

