from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import get_settings
from typing import Generator

settings = get_settings()

engine = create_engine(settings.URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()