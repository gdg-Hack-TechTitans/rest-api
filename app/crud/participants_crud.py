from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app import models
from ..schemas import participants_schemas

def create_participant(db: Session, participant: participants_schemas.ParticipantCreate):
    hashed_password = bcrypt.hash(participant.password)
    db_participant = models.Participant(**participant.model_dump(), hashed_password=hashed_password)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant