from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash

from src.users.user_dtos import UserSchema, LoginSchema
from src.users.user_model import UserModel

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register_user(body: UserSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, "User already exists with this username")

    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(400, "User already exists with this email")

    hash_pass = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        password = hash_pass,
        email = body.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return { "status": True, "message": "User registration successful!", "data": new_user }

def login_user(body, db:Session):
    print(body)
    return { "status": True, "message": "User login successful!", "data": "" }