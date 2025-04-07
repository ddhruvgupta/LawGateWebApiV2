import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from icecream import ic

# Replace with your own credentials
DATABASE_URL = os.getenv("DATABASE_URL")
ic(DATABASE_URL)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
