from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlapp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()