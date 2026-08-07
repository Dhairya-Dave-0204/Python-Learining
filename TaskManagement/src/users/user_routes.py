from fastapi import APIRouter, Depends, status, Request, BackgroundTasks
from sqlalchemy.orm import Session

from src.users.user_dtos import UserSchema, LoginSchema
from src.utils.db import get_db
from src.users import user_controller

user_router = APIRouter(prefix="/user")

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(body:UserSchema, bg_task: BackgroundTasks, db:Session = Depends(get_db)):
    return await user_controller.register_user(body, bg_task, db)

@user_router.post("/login", status_code= status.HTTP_200_OK)
def login_user(body: LoginSchema, db:Session = Depends(get_db)):
    return user_controller.login_user(body, db)

@user_router.get("/is-authenticated", status_code= status.HTTP_200_OK)
def is_authenticated(request: Request, db:Session = Depends(get_db)):
    return user_controller.is_authenticated(request, db)