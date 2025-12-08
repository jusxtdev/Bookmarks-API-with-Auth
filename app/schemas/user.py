from pydantic import BaseModel
from datetime import datetime

from app.schemas.resource import ResourceResponse

class UserCreate(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    user_id : int
    username : str
    hashed_passw : str | None = None
    
    create_at : datetime
    update_at : datetime | None = None

    resources : list[ResourceResponse] | None = None
    
    model_config = {"from_attributes": True}