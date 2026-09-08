from pydantic import BaseModel


class Movie(BaseModel):
    Movie_name: str
    Theatre_name: str
    Ticket_price: int
    description: str
    language: str = "Telugu"
    total_seats: int = 100


class BookingCreate(BaseModel):
    movie_name: str
    language: str
    seats_to_book: int