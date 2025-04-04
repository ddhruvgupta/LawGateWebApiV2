from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Replace with your own credentials
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/your_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
