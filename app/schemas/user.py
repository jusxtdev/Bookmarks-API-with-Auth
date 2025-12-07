from pydantic import BaseModel
from datetime import datetime

from app.models.resources import Resource

class UserCreate(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    username : str
    password : str
    
    create_at : datetime
    update_aat : datetime

    resources : list[Resource]   