from sqlalchemy.orm import Session
from ..schemas import teams_schemas
from app import models

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: teams_schemas.TeamCreate):
    db_team = models.Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if db_team:
        db.delete(db_team)
        db.commit()
        return db_team  # Return the deleted team
    return None  # Return None if the team doesn't exist

def update_team(db: Session, team_id: int, team: teams_schemas.TeamCreate):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if db_team:
        for key, value in team.model_dump().items():
            setattr(db_team, key, value)
        db.commit()
        db.refresh(db_team)
    return db_team
