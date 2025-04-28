import csv
from app.db.database import SessionLocal
from app.models.movie import Movie

def load_csv_to_db(csv_file_path: str):
    db = SessionLocal()
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=';')
                        
            for row in csv_reader:                
                movie = Movie(
                    year=int(row["year"]),
                    title=row["title"],
                    studios=row["studios"],
                    producers=row["producers"],
                    winner=row["winner"].strip().lower() == "yes"
                )
                db.add(movie)

            db.commit()

    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")
    finally:
        db.close()

