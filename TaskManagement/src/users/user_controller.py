from sqlalchemy.orm import Session

from src.users.user_dtos import UserSchema


def register_user(body: UserSchema, db: Session):
    print(body)
    return { "status": True, "message": "User registration successful!" }