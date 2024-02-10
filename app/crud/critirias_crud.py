from sqlalchemy.orm import Session
from app import models
from ..schemas import critirias_schemas


def create_criteria(db: Session, criteria: critirias_schemas.CriteriaCreate):
    db_criteria = models.Criteria(**criteria.model_dump())
    db.add(db_criteria)
    db.commit()
    db.refresh(db_criteria)
    return db_criteria
