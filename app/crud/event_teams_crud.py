from sqlalchemy.orm import Session
from app import models

def get_event_teams_with_participants(db: Session, event_id: int):
    return (
        db.query(models.Team)
        .join(models.EventTeam, models.Team.id == models.EventTeam.id_team)
        .filter(models.EventTeam.id_event == event_id)
        .options(
            db.selectinload(models.Team.participants)
        )
        .all()
    )
