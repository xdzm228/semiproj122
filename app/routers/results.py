from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/results", tags=["Результати"])

@router.post("/")
def submit_result(result: schemas.ResultCreate, db: Session = Depends(database.get_db)):
    db_result = models.Result(
        tournament_id=result.tournament_id,
        team_id=result.team_id,
        score=result.score
    )
    db.add(db_result)

    team = db.query(models.Team).filter(models.Team.id == result.team_id).first()
    if team:
        team.rating += result.score * 10  # 🔢 Простий алгоритм рейтингу
        db.commit()
        db.refresh(team)

    db.commit()
    return {"message": "Результат додано", "team_new_rating": team.rating}

@router.get("/{tournament_id}", response_model=list[schemas.ResultOut])
def get_results(tournament_id: int, db: Session = Depends(database.get_db)):
    results = db.query(models.Result).filter(models.Result.tournament_id == tournament_id).all()
    return results
