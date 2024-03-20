from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from typing import Generator


print("Database URL is ", settings.SQLITE_DB_URL)
engine = create_engine(settings.SQLITE_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
