from fastapi import FastAPI
from models import User, Transaction
from database import SessionLocal

app = FastAPI()

@app.get("/user/{telegram_id}")
def get_user(telegram_id: str):
    db = SessionLocal()
    user = db.query(User).filter(User.telegram_id==telegram_id).first()
    return {"user": {"username": user.username, "level": user.level, "balance": user.balance}}