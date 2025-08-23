# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import DATABASE_URL

# =========================
# Engine তৈরি করা হচ্ছে
# =========================
# connect_args={"check_same_thread": False} শুধুমাত্র SQLite এর জন্য প্রয়োজন
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite-এ প্রয়োজন
)

# =========================
# Session তৈরি করা হচ্ছে
# =========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =========================
# Base Class
# =========================
Base = declarative_base()

# =========================
# Helper function
# =========================
def get_db():
    """
    FastAPI dependency হিসেবে ব্যবহার করা যাবে
    db session provide করতে
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()