from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from config.config import Config


def get_session():
    engine = create_engine(
        Config.DATABASE_URI,
        echo=True,
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    return SessionLocal()