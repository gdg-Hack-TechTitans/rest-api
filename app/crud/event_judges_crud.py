from sqlalchemy.orm import Session
from app import models
from ..schemas import event_judges_schemas

def get_event_judges(db: Session, event_id: int):
    return (
        db.query(models.Judge)
        .join(models.EventJudge, models.Judge.id == models.EventJudge.id_judge)
        .filter(models.EventJudge.id_event == event_id)
        .all()
    )

def create_event_judge(db: Session, event_judge: event_judges_schemas.EventJudgeCreate):
    db_event_judge = models.EventJudge(**event_judge.model_dump())
    db.add(db_event_judge)
    db.commit()
    db.refresh(db_event_judge)
    return db_event_judge