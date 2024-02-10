from sqlalchemy.orm import Session
from app import models

def get_event_speakers(db: Session, event_id: int):
    return (
        db.query(models.Speaker)
        .join(models.EventSpeaker, models.Speaker.id == models.EventSpeaker.id_speaker)
        .filter(models.EventSpeaker.id_event == event_id)
        .all()
    )