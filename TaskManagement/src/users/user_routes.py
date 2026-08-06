from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.users.user_dtos import UserSchema
from src.utils.db import get_db
from src.users import user_controller

user_router = APIRouter(prefix="/user")

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(body:UserSchema, db:Session = Depends(get_db)):
    return user_controller.register_user(body, db)