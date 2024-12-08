import os
from sqlalchemy import Column, Integer, String, Boolean, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Basis-Klasse für alle SQLAlchemy-Modelle
Base = declarative_base()


class User(Base):
    __tablename__ = 'user_data'
    index = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Email = Column(String)
    Adresse = Column(String)
    Geburtsdatum = Column(Date)


# SQLite-Engine und Session-Setup

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    'postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase'
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
