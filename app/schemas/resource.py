from pydantic import BaseModel
from datetime import datetime

class ResourceCreate(BaseModel):
    title : str
    url : str
    description : str | None = None
    
class ResourceUpdate(BaseModel):
    title : str | None = None
    url : str | None = None
    description : str | None = None

class ResourceResponse(BaseModel):
    resource_id : int
    title : str
    url : str
    description : str
    user_id : int | None
    user : int | None
    create_at : datetime
    update_at : datetime