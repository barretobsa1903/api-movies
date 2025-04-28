from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.movie_service import  get_producers_intervals_min_max
from app.db.database import SessionLocal

router = APIRouter(
    prefix="/api/v1/movies",
    tags=["movies"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/producers-intervals")
def get_producers_intervals(db: Session = Depends(get_db)):
    intervals = get_producers_intervals_min_max(db)
    return intervals