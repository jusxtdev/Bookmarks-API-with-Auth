from fastapi import HTTPException, status

def raise_error_404(entity):
    '''
    entity : Any => Entity to validate
    '''
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= 'Requested Data was not found'
        )