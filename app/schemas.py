from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TeamCreate(BaseModel):
    name: str
    owner_id: int

class TeamOut(BaseModel):
    id: int
    name: str
    rating: float

    class Config:
        orm_mode = True

class TournamentCreate(BaseModel):
    name: str
    game: str

class TournamentOut(BaseModel):
    id: int
    name: str
    game: str
    date: datetime

    class Config:
        orm_mode = True

class ResultCreate(BaseModel):
    tournament_id: int
    team_id: int
    score: float

class ResultOut(BaseModel):
    team: TeamOut
    score: float
