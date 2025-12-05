from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey

from app.database import Base

class Template(Base):
    __tablename__ = "templates"