from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

from .blog import Blog

class User(Base):
    __tablename__ = "users"     
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False,index=True)
    password = Column(String, nullable=False)   
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="author")
