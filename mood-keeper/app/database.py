"""Database models and configuration using SQLAlchemy"""
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(ROOT, 'data', 'mood_keeper.db')
DATABASE_URL = f'sqlite:///{DB_PATH}'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Account(Base):
    """User account model"""
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True, index=True)
    handle = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, nullable=False)
    hashed = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.now)


class Entry(Base):
    """Mood and habits entry model"""
    __tablename__ = 'entries'
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, nullable=False)
    handle = Column(String, nullable=False)
    mood = Column(Integer, nullable=False)  # 1-10
    comment = Column(Text, nullable=True)
    
    # Nuevos campos de hábitos
    horas_sueno = Column(Float, nullable=True)  # Horas de sueño
    actividad_fisica = Column(Integer, nullable=True)  # 0-10 nivel de actividad
    calidad_alimentacion = Column(Integer, nullable=True)  # 0-10 calidad
    nivel_socializacion = Column(Integer, nullable=True)  # 0-10 nivel
    
    created = Column(DateTime, default=datetime.now)


def init_db():
    """Initialize database and create tables"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    Base.metadata.create_all(bind=engine)


def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
