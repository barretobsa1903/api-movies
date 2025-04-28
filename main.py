
from fastapi import FastAPI
from app.utils.csv_loader import load_csv_to_db
from app.db.database import init_db
import os
from app.api.routes import router as api_router  
from app.models.movie import Movie
from sqlalchemy import inspect
from app.db.database import engine

app = FastAPI()

init_db()

inspector = inspect(engine)
tables = inspector.get_table_names()

csv_file_path = os.path.join(os.path.dirname(__file__), "Movielist[1].csv")
load_csv_to_db(csv_file_path)

app.include_router(api_router)  


