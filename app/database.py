from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Change Database URL
DATABASE_URL = 'sqlite:///./database.db'

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread' : False}  # For SQLITE Only
    )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()