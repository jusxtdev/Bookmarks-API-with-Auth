from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from typing import Annotated
from app.utils.common import verify_password
from app.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

db_dependency = Annotated[Session, Depends(get_db)]

@router.post('/login', status_code=status.HTTP_200_OK)
def login(db : db_dependency,login_credentials : OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.username == login_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Credentials')
    
    isCorrectPassw = verify_password(login_credentials.password, user.hashed_passw)

    if not isCorrectPassw:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')

    access_token = create_access_token(data={'sub' : user.username})
    return {'access_token' : access_token, "token_type" : "bearer"}