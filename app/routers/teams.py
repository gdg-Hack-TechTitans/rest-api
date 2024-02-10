from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import teams_schemas
from ..crud import teams_crud


team_router = APIRouter()

@team_router.post("/v1/teams/", response_model=teams_schemas.Team, status_code=201)
def create_team(team: teams_schemas.TeamCreate, db: Session = Depends(get_db)):
    return teams_crud.create_team(db=db, team= team)

@team_router.get("/v1/teams/", response_model=list[teams_schemas.Team])
def get_teams(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return teams_crud.get_teams(db, skip, limit)

@team_router.get("/v1/teams/{team_id}/", response_model=teams_schemas.Team)
def get_team(team_id: int , db: Session = Depends(get_db)):
    db_team= teams_crud.get_team(db,team_id=team_id)
    print(db_team)
    if db_team is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_team

@team_router.delete("/v1/teams/{team_id}/", response_model=teams_schemas.Team)
def delete_team(team_id: int , db: Session = Depends(get_db)):
    deleted_team = teams_crud.delete_team(db, team_id=team_id)

    if deleted_team is None:
        raise HTTPException(status_code=404, detail="Team not found")

    return deleted_team

@team_router.put("/v1/teams/{team_id}/", response_model=teams_schemas.Team)
def update_team(team_id: int ,team: teams_schemas.TeamCreate, db: Session = Depends(get_db)):
    return teams_crud.update_team(db, team_id=team_id, team=team)
