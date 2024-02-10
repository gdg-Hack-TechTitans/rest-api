from app.utilities import generate_random_password, hash_password
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app import models
from ..schemas import mentors_schemas


def create_mentor(db: Session, mentor: mentors_schemas.MentorCreate):
    random_password = generate_random_password()
    hashed_password = hash_password(random_password)
    db_mentor = models.Mentor(**mentor.model_dump(), password=hashed_password)
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    return db_mentor, random_password

def get_all_mentors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mentor).offset(skip).limit(limit).all()

def get_mentor(db: Session, mentor_id: int):
    return db.query(models.Mentor).filter(models.Mentor.id == mentor_id).first()

def delete_mentor(db: Session, mentor_id: int):
    mentor = db.query(models.Mentor).filter(models.Mentor.id == mentor_id).first()
    if mentor:
        db.delete(mentor)
        db.commit()
        return mentor
    
def update_mentor(db: Session, mentor_id: int, updated_mentor: mentors_schemas.MentorCreate):
    existing_mentor = db.query(models.Mentor).filter(models.Mentor.id == mentor_id).first()

    if existing_mentor:
        for key, value in updated_mentor.model_dump().items():
            setattr(existing_mentor, key, value)

        db.commit()
        db.refresh(existing_mentor)
        return existing_mentor