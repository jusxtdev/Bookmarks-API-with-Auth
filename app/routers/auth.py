from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.authentication import Login
from app.schemas.user import UserResponse
from app.database import get_db
from app.models.users import User
from typing import Annotated
from app.utils.common import verify_password
from app.token import create_access_token

router = APIRouter(tags=['Authentication'])

db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/login', response_model=dict, status_code=status.HTTP_200_OK)
def login(login_credentials : Login, db : db_dependency):
    user = db.query(User).filter(User.username == login_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Credentials')
    
    isCorrectPassw = verify_password(login_credentials.password, user.hashed_passw)

    if not isCorrectPassw:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')

    access_token = create_access_token(data={'sub' : user.username})
    return {'access_token' : access_token, "token_type" : "bearer"}