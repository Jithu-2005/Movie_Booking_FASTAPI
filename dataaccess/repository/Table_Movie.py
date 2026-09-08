from dataaccess.data_models import Movie

from sqlalchemy.orm import Session



class MovieRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_movie(self, movie: Movie):

        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def get_all_Movies(self):
        return self.db.query(Movie).all()


    def get_movie_by_id(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.id == movie_id).first()


    def update_movie(self, movie_id: int, movie_data: dict):
        # Find the movie by ID and update it with the new data
        self.db.query(Movie).filter(Movie.id == movie_id).update(movie_data)
        self.db.commit()
        return {"status": "Updated"}


    def delete_movie(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.id == movie_id).first()


    def get_movie_seats(self, movie_id: int):
            return self.db.query(Movie).filter(Movie.id == movie_id).first()


    def get_movies_by_language(self, language: str):
        return self.db.query(Movie).filter(Movie.language.ilike(language)).all()