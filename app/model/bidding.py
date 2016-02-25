from sqlalchemy import Column, Integer

from ..database import Base

class Bidding(Base):
    __tablename__ = "bidding"

    bidding_url = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass
