from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import get_db

# Import models
from app.models.resources import Resource

# Import schemas
from app.schemas.resource import ResourceCreate, ResourceResponse, ResourceUpdate

from app.utils.common import raise_error_404

router = APIRouter(
    prefix = '/resource',     # Specify prefix for this route
    tags = ['Resources']
)

db_dependency = Annotated[Session, Depends(get_db)]

# POST Routes
@router.post('/', response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
def add_resource(new_data : ResourceCreate, db : db_dependency):
    new_resource = Resource(title=new_data.title, url=new_data.url,description=new_data.description)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

# GET Routes
@router.get('/', response_model=list[ResourceResponse], status_code=status.HTTP_200_OK)
def get_resources(db : db_dependency):
    all_resources = db.query(Resource).all()
    return all_resources

@router.get('/{resource_id}', response_model=ResourceResponse, status_code=status.HTTP_200_OK)
def get_resource_by_ID(resource_id : int, db : db_dependency):
    requested = db.query(Resource).where(Resource.resource_id == resource_id).first()
    raise_error_404(requested)
    return requested

# PUT Routes

# DELETE Routes