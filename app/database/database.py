from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL

from core.config import settings



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

url_object = URL.create(settings.POSTGRES_ENGINE, 
                        settings.POSTGRES_USER, 
                        settings.POSTGRES_PASSWORD, 
                        settings.POSTGRES_HOST, 
                        settings.POSTGRES_PORT,
                        settings.POSTGRES_DATABASE,
                        )

# Criando o motor de conexão
engine = create_engine(url_object)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

