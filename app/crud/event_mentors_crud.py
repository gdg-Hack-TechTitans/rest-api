from sqlalchemy.orm import Session
from app import models 

def get_event_mentors(db: Session, event_id: int):
    return (
        db.query(models.Mentor)
        .join(models.EventMentor, models.Mentor.id == models.EventMentor.id_mentor)
        .filter(models.EventMentor.id_event == event_id)
        .all()
    )