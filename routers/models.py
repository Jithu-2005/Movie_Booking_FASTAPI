from pydantic import BaseModel


class Movie(BaseModel):
    Movie_name: str
    Theatre_name: str
    Ticket_price: int
    Description: str
    Language: str = "Telugu"
    Total_seats: int = 100


class BookingCreate(BaseModel):
    movie_id: int
    seats_to_book: int