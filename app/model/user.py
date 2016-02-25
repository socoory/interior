from sqlalchemy import Column, String, Integer, DateTime

from ..database import Base

class User(Base):
    __tablename__ = 'user'

    user_srl = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, index=True)
    password = Column(String(64), nullable=True)
    name = Column(String(32), nullable=True)
    user_type = Column(String(15), nullable=False)
    regdate = Column(DateTime)

    def __init__(self):
        pass