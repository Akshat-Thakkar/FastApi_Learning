from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)   
    content = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
