import os
from dotenv import load_dotenv
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "My FastAPI Application"
    PROJECT_VERSION: str = "0.1.0"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sqlapp.db"

settings = Settings()
