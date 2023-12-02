
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime
from db.base_class import Base


class Book(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    isbn = Column(String,  nullable=False, unique=True, index=True)
    author = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)