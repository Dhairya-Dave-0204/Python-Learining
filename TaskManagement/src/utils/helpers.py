from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session

import jwt
from jwt.exceptions import InvalidTokenError

from src.utils.settings import settings
from src.users.user_model import UserModel
from src.utils.db import get_db

def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(401, "Token expired for user, login again")
            
        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.JWT_SECRET_KEY, settings.ALGORITHM)

        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(401, "No user found with this token")
        
        return user
    except InvalidTokenError:
        raise HTTPException(401, "User authentication failed!")