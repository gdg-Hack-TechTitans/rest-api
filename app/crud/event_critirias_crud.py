from sqlalchemy.orm import Session
from app import models
from ..schemas import event_critirias_schemas

def create_event_criteria(db: Session, event_criteria: event_critirias_schemas.EventCriteriaCreate):
    db_event_criteria = models.EventCriteria(**event_criteria.model_dump())
    db.add(db_event_criteria)
    db.commit()
    db.refresh(db_event_criteria)
    return db_event_criteria
