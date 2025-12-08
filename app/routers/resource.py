from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import datetime

from app.database import get_db
from app import oauth2
# Import models
from app.models.resources import Resource

# Import schemas
from app.schemas.resource import ResourceCreate, ResourceResponse, ResourceUpdate
from app.schemas.user import UserResponse
from app.utils.common import raise_error_404

router = APIRouter(
    prefix = '/resource',     # Specify prefix for this route
    tags = ['Resources']
)

db_dependency = Annotated[Session, Depends(get_db)]

# POST Routes
@router.post('/', response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
def add_resource(new_data : ResourceCreate, db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    new_resource = Resource(title=new_data.title, url=new_data.url,description=new_data.description)
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

# GET Routes
@router.get('/', response_model=list[ResourceResponse], status_code=status.HTTP_200_OK)
def get_resources(db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    all_resources = db.query(Resource).all()
    return all_resources

@router.get('/{resource_id}', response_model=ResourceResponse, status_code=status.HTTP_200_OK)
def get_resource_by_ID(resource_id : int, db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    requested = db.query(Resource).where(Resource.resource_id == resource_id).first()
    raise_error_404(requested)
    return requested

# PUT Routes
@router.put('/{resource_id}', response_model=ResourceResponse, status_code=status.HTTP_200_OK)
def update_resource(resource_id : int ,resource_data : ResourceUpdate, db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    existing_resource = db.query(Resource).where(Resource.resource_id == resource_id).first()
    raise_error_404(existing_resource)

    update_data = resource_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_resource, key, value)
    
    existing_resource.update_at = datetime.now().replace(microsecond=0)

    db.commit()
    db.refresh(existing_resource)
    return existing_resource

# DELETE Routes
@router.delete('/{resource_id}', response_model=ResourceResponse, status_code=status.HTTP_200_OK)
def delete_resource(resource_id : int, db : db_dependency, get_current_user : UserResponse = Depends(oauth2.get_current_user)):
    requested_resource = db.query(Resource).where(Resource.resource_id == resource_id).first()
    raise_error_404(requested_resource)

    db.delete(requested_resource)
    db.commit()
    return requested_resource