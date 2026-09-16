from pydantic import BaseModel


class Movie(BaseModel):
    Movie_name: str
    Theatre_name: str
    Ticket_price: int
    description: str
    language: str = "Telugu"
    total_seats: int = 100


class BookingCreate(BaseModel):
    movie_id: int
    seats: int
    user_id: str = ""