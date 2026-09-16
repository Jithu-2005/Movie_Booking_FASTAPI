from sqlalchemy.orm import Session
from dataaccess.repository.Table_Movie import MovieRepository
from dataaccess.repository.Table_Booking import BookingRepository,Movie
from business_logic.models import BookingCreate, MovieCreate
from dataaccess.data_models import Booking


class Servicelayer:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.movie_repo = MovieRepository(self.db_session)
        self.booking_repo = BookingRepository(self.db_session)

    def create_movie(self, movie: MovieCreate):
        create_movie = Movie(
            Movie_name = movie.Movie_name,
            Theatre_name = movie.Theatre_name,
            Ticket_price = movie.Ticket_price,
            description = movie.description,
            language = movie.language,
            total_seats = movie.total_seats
        )
        db_result = self.movie_repo.add_movie(create_movie)
        return MovieCreate.from_db(db_result)


    def get_all_movies(self):
        return self.db_session.query(Movie).all()


    def get_movie_by_id(self, movie_id: int):
        return self.db_session.query(Movie).filter(Movie.id == movie_id).first()


    def update_movie(self, movie_id: int, movie_data: MovieCreate):
        return self.movie_repo.update_movie(movie_id, movie_data.model_dump())


    def delete_movie(self, movie_id: int):
        return self.movie_repo.delete_movie(movie_id)


    def book_tickets(self, booking_data: BookingCreate):
        movie = self.db_session.query(Movie).filter(Movie.Movie_name == booking_data.movie_name).first()
        if not movie:
            raise ValueError("Movie not found")
        calculated_total = movie.Ticket_price * booking_data.seats_to_book
        book_tickets = Booking(
            movie_name = booking_data.movie_name,
            seats_to_book = booking_data.seats_to_book,
            language = booking_data.language,
            total_amount = calculated_total
        )
        db_result = self.booking_repo.add_booking(book_tickets)
        movie.total_seats -= booking_data.seats_to_book
        self.db_session.commit()
        return BookingCreate.from_db(db_result)


    def get_booking_details(self, booking_id: int):

        return self.booking_repo.get_booking_by_id(booking_id)

    def cancel_booking(self, booking_id: int):
        booking = self.booking_repo.get_booking_by_id(booking_id)
        if not booking:
            return False
        
        movie = self.db_session.query(Movie).filter(Movie.Movie_name == booking.movie_name).first()
        if movie:
            movie.total_seats += booking.seats_to_book
            self.db_session.commit()

        return self.booking_repo.delete_booking(booking_id)

    def get_available_seats(self, movie_id: int):
        movie = self.get_movie_by_id(movie_id)
        if not movie:
            return None
        return movie.total_seats


    def get_movies_by_language(self, language: str):
        return self.movie_repo.get_movies_by_language(language)