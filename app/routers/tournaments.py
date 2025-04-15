from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/tournaments", tags=["Турніри"])

@router.post("/", response_model=schemas.TournamentOut)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(database.get_db)):
    db_tour = models.Tournament(name=tournament.name, game=tournament.game)
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour

@router.get("/", response_model=list[schemas.TournamentOut])
def list_tournaments(db: Session = Depends(database.get_db)):
    return db.query(models.Tournament).all()
