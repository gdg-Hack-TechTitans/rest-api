from sqlalchemy.orm import Session
from app import models

def get_event_lost_objects(db: Session, event_id: int): 
    return(
        db.query(models.LostObject)
        .filter(models.LostObject.id_event == event_id)
        .all()
    )
