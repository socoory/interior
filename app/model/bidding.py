from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from ..database import Base

class Bidding(Base):
    __tablename__ = "bidding"

    bidding_url = Column(Integer, primary_key=True, autoincrement=True)

    auction = relationship('Auction', ForeignKey('auction.auction_srl'))

    def __init__(self):
        pass
