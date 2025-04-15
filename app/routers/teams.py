from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/teams", tags=["Команди"])

@router.post("/", response_model=schemas.TeamOut)
def create_team(team: schemas.TeamCreate, db: Session = Depends(database.get_db)):
    db_team = models.Team(name=team.name, owner_id=team.owner_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

@router.get("/", response_model=list[schemas.TeamOut])
def list_teams(db: Session = Depends(database.get_db)):
    return db.query(models.Team).all()
