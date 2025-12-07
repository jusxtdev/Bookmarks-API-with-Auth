from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#! Import models here to prevent this error
# sqlalchemy.exc.NoReferencedTableError:
#       Foreign key associated with column 'resources.user_id'
#       could not find table 'users' with which to generate a
#       foreign key to target column 'user_id'

from app.models.resources import Resource
from app.models.users import User
from app.base import Base

# Change Database URL
DATABASE_URL = 'sqlite:///./database.db'

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread' : False}  # For SQLITE Only
    )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()