from sqlalchemy.orm import Session
from app.models.movie import Movie
from collections import defaultdict
from app.repositories.movie_repository import get_all_winner_movies

class MovieService:
    
     @staticmethod
     def list_movies(db: Session):
        return db.query(Movie).all() 
   
def get_producers_intervals_min_max(db: Session):
    movies = get_winner_movies(db)
    producers_prizes = group_movies_by_producer(movies)
    min_intervals, max_intervals = calculate_intervals(producers_prizes)
    
    return {"min": min_intervals, "max": max_intervals}


def get_winner_movies(db: Session):
    movies = get_all_winner_movies(db)
    return movies


def group_movies_by_producer(movies):
    from collections import defaultdict
    producers_prizes = defaultdict(list)
    for movie in movies:
        producers_prizes[movie.producers].append(movie.year)
    return producers_prizes


def calculate_intervals(producers_prizes):
    min_interval = float('inf') 
    max_interval = -1  
    min_interval_data = defaultdict(list)
    max_interval_data = defaultdict(list)

    for producer, years in producers_prizes.items():
        years.sort()
        for i in range(1, len(years)):
            previous_win = years[i - 1]
            following_win = years[i]
            interval = following_win - previous_win

            if interval > 0 and (min_interval is None or interval < min_interval):
                min_interval = interval
                min_interval_data = defaultdict(list)  
                min_interval_data[producer].append(build_interval(producer, interval, previous_win, following_win))
            elif interval == min_interval:
                min_interval_data[producer].append(build_interval(producer, interval, previous_win, following_win))

            if interval > 0 and (max_interval is None or interval > max_interval):
                max_interval = interval
                max_interval_data = defaultdict(list)  
                max_interval_data[producer].append(build_interval(producer, interval, previous_win, following_win))
            elif interval == max_interval:
                max_interval_data[producer].append(build_interval(producer, interval, previous_win, following_win))

    min_intervals = list({item["producer"]: item for sublist in min_interval_data.values() for item in sublist}.values())
    max_intervals = list({item["producer"]: item for sublist in max_interval_data.values() for item in sublist}.values())

    return min_intervals, max_intervals

def build_interval(producer, interval, previous_win, following_win):
    return {
        "producer": producer,
        "interval": interval,
        "previousWin": previous_win,
        "followingWin": following_win
    }