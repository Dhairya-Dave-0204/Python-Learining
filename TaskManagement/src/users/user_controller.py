from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta

from src.users.user_dtos import UserSchema, LoginSchema
from src.users.user_model import UserModel
from src.utils.settings import settings

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(original, hashed):
    return password_hash.verify(original, hashed)

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

def login_user(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(401, "No user found with this username")
    
    if not verify_password(body.password, user.password):
        raise HTTPException(401, "Incorrect password for this user")        

    exp_time = datetime.now() + timedelta(minutes= settings.EXP_TIME)

    token = jwt.encode(
        { 
            "_id": user.id, 
            "username": user.username,
            "exp": exp_time 
        }, 
        settings.JWT_SECRET_KEY, 
        settings.ALGORITHM
    )



    return { 
        "status": True, 
        "message": "User login successful!", 
        "data": user, 
        "token": token 
    }