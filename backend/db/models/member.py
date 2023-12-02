from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime
from db.base_class import Base


class Member(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
