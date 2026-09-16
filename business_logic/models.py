from pydantic import BaseModel

from dataaccess.data_models import Booking, Movie

class Movie(BaseModel):
    Movie_name: str
    Theatre_name: str
    Ticket_price: int
    description: str
    language: str
    total_seats: int


    @classmethod
    def from_db(cls, db_model: Movie):
        return cls(
            Movie_name = db_model.Movie_name,
            Theatre_name = db_model.Theatre_name,
            Ticket_price = db_model.Ticket_price,
            description = db_model.description,
            language = db_model.language,
            total_seats = db_model.total_seats
        )


class BookingCreate(BaseModel):
    movie_name: str
    seats_to_book: int
    language: str
    
    @classmethod
    def from_db(cls, db_model: Booking):
        return cls(
            movie_name = db_model.movie_name,
            seats_to_book = db_model.seats_to_book,
            language = db_model.language,
        )





    