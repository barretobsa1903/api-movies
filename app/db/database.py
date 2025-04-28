from sqlalchemy import create_engine, Column, Integer, String,Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

SQLALCHEMY_DATABASE_URL = "sqlite:///./bd_movies.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session_local(engine_override=None):
    if engine_override:
        return sessionmaker(autocommit=False, autoflush=False, bind=engine_override)
    return SessionLocal

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    title = Column(String, index=True)
    studios = Column(String)
    producers = Column(String)
    winner = Column(Boolean, default=False)

def init_db():
    Base.metadata.create_all(bind=engine)
    
    inspector = inspect(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

init_db()
