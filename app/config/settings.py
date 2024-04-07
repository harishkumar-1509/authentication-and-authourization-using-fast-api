import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings
import urllib.parse
from functools import lru_cache

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME","FastAPIAuthApp")
    DEBUG: bool = bool(os.getenv("DEBUG",False))
    
    DB_HOST: str = os.getenv("DB_HOST")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    
    encoded_password = urllib.parse.quote_plus(DB_PASSWORD)
    URL_DATABASE = f"postgresql://{DB_USERNAME}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    SECRET_KEY: str = os.getenv("SECRET_KEY")

@lru_cache
def get_settings() -> Settings:
    return Settings()