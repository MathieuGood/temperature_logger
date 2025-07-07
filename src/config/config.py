from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE_URI: str = os.getenv("DATABASE_URI") or ""
    TEST_DATABASE_URI: str = os.getenv("TEST_DATABASE_URI") or ""
    SECRET_KEY: str = os.getenv("SECRET_KEY") or ""
    TOKEN: str = os.getenv("TOKEN") or ""
    REQUEST_INTERVAL: int = int(os.getenv("REQUEST_INTERVAL") or "60")
    VERBOSE_SQL_LOGGING: bool = (
        str(os.getenv("VERBOSE_SQL_LOGGING")).lower() == "true" or False
    )
