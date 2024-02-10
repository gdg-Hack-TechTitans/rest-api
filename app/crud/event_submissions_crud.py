from sqlalchemy.orm import Session
from app import models, schemas


def create_event_submission(db: Session, event_submission: schemas.EventSubmissionCreate):
    db_event_submission = models.EventSubmission(**event_submission.model_dump())
    db.add(db_event_submission)
    db.commit()
    db.refresh(db_event_submission)
    return db_event_submission


def get_event_submissions(db: Session, event_id: int):
    return (
        db.query(models.EventSubmission)
        .filter(models.EventSubmission.id_event == event_id)
        .options(
            db.selectinload(models.EventSubmission.team),
            db.selectinload(models.EventSubmission.field),
        )
        .all()
    )
