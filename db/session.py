from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from chatbot_2.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.db.uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()