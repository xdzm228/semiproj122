from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, auth, database

router = APIRouter(prefix="/users", tags=["Користувачі"])

@router.post("/", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
