import json
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE_URI: str = os.getenv("DATABASE_URI")
    TEST_DATABASE_URI: str = os.getenv("TEST_DATABASE_URI")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOKEN: str = os.getenv("TOKEN")
    REQUEST_INTERVAL: int = int(os.getenv("REQUEST_INTERVAL"))
    VERBOSE_SQL_LOGGING: bool = os.getenv("VERBOSE_SQL_LOGGING").lower() == "true"
