from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    username = Column(String)
    level = Column(Integer, default=0)
    balance = Column(Float, default=0.0)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    type = Column(String)  # deposit / withdraw
    amount = Column(Float)
    status = Column(String, default="pending")  # pending / approved / rejected
    created_at = Column(DateTime, default=datetime.datetime.utcnow)