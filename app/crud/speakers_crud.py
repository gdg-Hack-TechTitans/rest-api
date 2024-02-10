from app.utilities import generate_random_password, hash_password
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app import models
from ..schemas import speakers_schemas


def create_speaker(db: Session, speaker: speakers_schemas.SpeakerCreate):
    random_password = generate_random_password()
    hashed_password = hash_password(random_password)
    db_speaker = models.Speaker(**speaker.model_dump(), password=hashed_password)
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker, random_password

def get_all_speakers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Speaker).offset(skip).limit(limit).all()

def get_speaker(db: Session, speaker_id: int):
    return db.query(models.Speaker).filter(models.Speaker.id == speaker_id).first()

def delete_speaker(db: Session, speaker_id: int):
    speaker = db.query(models.Speaker).filter(models.Speaker.id == speaker_id).first()
    if speaker:
        db.delete(speaker)
        db.commit()
        return speaker
    
def update_speaker(db: Session, speaker_id: int, updated_speaker: speakers_schemas.SpeakerCreate):
    existing_speaker = db.query(models.Speaker).filter(models.Speaker.id == speaker_id).first()

    if existing_speaker:
        for key, value in updated_speaker.model_dump().items():
            setattr(existing_speaker, key, value)

        db.commit()
        db.refresh(existing_speaker)
        return existing_speaker