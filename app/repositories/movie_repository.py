from sqlalchemy.orm import Session
from app.models.movie import Movie

def get_all_winner_movies(db: Session):
    return db.query(Movie).filter(Movie.winner == True).order_by(Movie.producers, Movie.year).all()
