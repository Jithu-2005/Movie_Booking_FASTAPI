from pydantic import BaseModel


class Movie(BaseModel):
    movie_name: str
    theatre_name: str
    ticket_price: int
    description: str
    language: str = "Telugu"
    total_seats: int = 100


class BookingCreate(BaseModel):
    movie_id: int
    seats_to_book: int