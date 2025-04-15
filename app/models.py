from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    teams = relationship("Team", back_populates="owner")

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float, default=1000)

    owner = relationship("User", back_populates="teams")
    results = relationship("Result", back_populates="team")

class Tournament(Base):
    __tablename__ = "tournaments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    game = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    results = relationship("Result", back_populates="tournament")

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    score = Column(Float)

    tournament = relationship("Tournament", back_populates="results")
    team = relationship("Team", back_populates="results")
