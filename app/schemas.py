from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import date



class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }

class Token(BaseModel):
    access_token: str
    token_type: str


class PlaceBase(BaseModel):
    name: str
    description: Optional[str]
    country: str
    visited: bool
    date: Optional[date] = None

    model_config = {
        "from_attributes": True
    }


class PlaceCreate(PlaceBase):
    user_id: int


class Place(PlaceBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
