from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import get_db
# Import models
from app.models.users import User
# Import schemas
from app.schemas.user import UserCreate, UserResponse

from app.utils.common import raise_error_404, hash_password, verify_password
from app import oauth2
router = APIRouter(
    prefix = '/users',     # Specify prefix for this route
    tags = ['User']
)

db_dependency = Annotated[Session, Depends(get_db)]


# POST Routes
@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def add_user(new_data : UserCreate, db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    new_user = User(username=new_data.username, hashed_passw=hash_password(new_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET Routes
@router.get('/', response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(db : db_dependency):
    all_users = db.query(User).all()
    return all_users

@router.get('/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id : int, db : db_dependency):
    requested_user = db.query(User).where(User.user_id == user_id).first()
    raise_error_404(requested_user)
    return requested_user

