from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from . import models, schemas

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event

def update_event(db: Session, event_id: int, event: schemas.EventUpdate):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        for key, value in event.dict().items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event

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

def get_event_mentors(db: Session, event_id: int):
    return (
        db.query(models.Mentor)
        .join(models.EventMentor, models.Mentor.id == models.EventMentor.id_mentor)
        .filter(models.EventMentor.id_event == event_id)
        .all()
    )

def get_event_judges(db: Session, event_id: int):
    return (
        db.query(models.Judge)
        .join(models.EventJudge, models.Judge.id == models.EventJudge.id_judge)
        .filter(models.EventJudge.id_event == event_id)
        .all()
    )

def get_event_speakers(db: Session, event_id: int):
    return (
        db.query(models.Speaker)
        .join(models.EventSpeaker, models.Speaker.id == models.EventSpeaker.id_speaker)
        .filter(models.EventSpeaker.id_event == event_id)
        .all()
    )

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

def get_event_lost_objects(db: Session, event_id: int): 
    return(
        db.query(models.LostObject)
        .filter(models.LostObject.id_event == event_id)
        .all()
    )



def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def create_participant(db: Session, participant: schemas.ParticipantCreate):
    hashed_password = bcrypt.hash(participant.password)
    db_participant = models.Participant(**participant.model_dump(), hashed_password=hashed_password)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def create_mentor(db: Session, mentor: schemas.MentorCreate):
    hashed_password = bcrypt.hash(mentor.password)
    db_mentor = models.Mentor(**mentor.model_dump(), hashed_password=hashed_password)
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    return db_mentor

def create_speaker(db: Session, speaker: schemas.SpeakerCreate):
    hashed_password = bcrypt.hash(speaker.password)
    db_speaker = models.Speaker(**speaker.model_dump(), hashed_password=hashed_password)
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker

def create_field(db: Session, field: schemas.FieldCreate):
    db_field = models.Field(**field.model_dump())
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

def create_criteria(db: Session, criteria: schemas.CriteriaCreate):
    db_criteria = models.Criteria(**criteria.model_dump())
    db.add(db_criteria)
    db.commit()
    db.refresh(db_criteria)
    return db_criteria

def create_event_criteria(db: Session, event_criteria: schemas.EventCriteriaCreate):
    db_event_criteria = models.EventCriteria(**event_criteria.model_dump())
    db.add(db_event_criteria)
    db.commit()
    db.refresh(db_event_criteria)
    return db_event_criteria

def create_event_submission(db: Session, event_submission: schemas.EventSubmissionCreate):
    db_event_submission = models.EventSubmission(**event_submission.model_dump())
    db.add(db_event_submission)
    db.commit()
    db.refresh(db_event_submission)
    return db_event_submission

def create_judge(db: Session, judge: schemas.JudgeCreate):
    hashed_password = bcrypt.hash(judge.password)
    db_judge = models.Judge(**judge.model_dump(), hashed_password=hashed_password)
    db.add(db_judge)
    db.commit()
    db.refresh(db_judge)
    return db_judge

def create_event_judge(db: Session, event_judge: schemas.EventJudgeCreate):
    db_event_judge = models.EventJudge(**event_judge.model_dump())
    db.add(db_event_judge)
    db.commit()
    db.refresh(db_event_judge)
    return db_event_judge