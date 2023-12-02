from datetime import datetime
from db.base_class import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .member import Member
from .order_detail import OrderDetail


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("member.id"))
    member = relationship("Member", back_populates="member")
    borrowed_date = Column(DateTime, default=datetime.now)
    returned_date = Column(DateTime)
    order_details = relationship("OrderDetail", back_populates="order_detail")
