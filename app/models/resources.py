from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Resource(Base):
    __tablename__ = 'resources'

    resource_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey('users.user_id'))     # relationship to User
    
    user = relationship('User', back_populates='resources') 

    create_at = Column(DateTime, default=datetime.now())
    update_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())