from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from ..database import Base

class Auction(Base):
    __tablename__ = 'auction'

    auction_srl = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(127), nullable=False)
    status = Column(String(31), nullable=False)
    start_price = Column(Integer, nullable=False)
    bid_price = Column(Integer, nullable=False)
    start_date = Column(DateTime(6), nullable=False)
    end_date = Column(DateTime(6), nullable=False)
    regdate = Column(DateTime(6), nullable=False)

    def __init__(self, title, status, start_price, bid_price, start_date, end_date):
        self.title = title
        self.status = status
        self.start_price = start_price
        self.bid_price = bid_price
        self.start_date = start_date
        self.end_date = end_date
        self.regdate = datetime.utcnow()