from fastapi import HTTPException, status
from passlib.context import CryptContext

def raise_error_404(entity):
    '''
    entity : Any => Entity to validate
    '''
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= 'Requested Data was not found'
        )
    

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated = 'auto'
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)