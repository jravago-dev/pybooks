from datetime import datetime
from db.base_class import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class OrderDetail(Base):
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", back_populates="book")
