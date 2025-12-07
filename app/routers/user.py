from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
# Import models
# Import schemas
from app.utils.common import raise_error_404

router = APIRouter(
    prefix = '',     # Specify prefix for this route
    tags = ['Tag']
)

