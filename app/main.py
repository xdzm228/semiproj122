from fastapi import FastAPI
from . import models, database
from .routers import teams, tournaments, results

models.Base.metadata.create_all(bind=database.engine)  # Створення таблиць

app = FastAPI()

app.include_router(teams.router)
app.include_router(tournaments.router)
app.include_router(results.router)