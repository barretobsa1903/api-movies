from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()



class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    studios = Column(String, nullable=False)
    producers = Column(String, nullable=False)
    winner = Column(Boolean, nullable=False)
    
    def __repr__(self):
        return f"<Movie(id={self.id}, year={self.year}, title={self.title}, producers={self.producers}, winner={self.winner})>"
