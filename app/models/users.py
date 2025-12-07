from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_passw = Column(String)
    create_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime, onupdate=datetime.now(), default=datetime.now())

    resources = relationship('Resource', back_populates='user')
    # Relationship to resources