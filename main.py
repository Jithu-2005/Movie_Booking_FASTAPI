from fastapi import FastAPI

from routers.movies import movie_app

app = FastAPI(title = "Movie Booking API")


app.include_router(movie_app)