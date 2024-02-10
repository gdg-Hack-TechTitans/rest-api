from sqlalchemy.orm import Session
from app import models

def get_event_fields_with_criteria(db: Session, event_id: int):
    return (
        db.query(models.Field)
        .join(models.Criteria, models.Field.name == models.Criteria.name_field)
        .join(models.EventCriteria, models.Field.name == models.EventCriteria.name_criteria)
        .filter(models.EventCriteria.id_event == event_id)
        .options(
            db.selectinload(models.Field.criteria)
        )
        .all()
    )