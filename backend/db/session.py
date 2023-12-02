from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSION_LOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SESSION_LOCAL()
        yield db
    finally:
        db.close()
