from app.utilities import generate_random_password, hash_password
from sqlalchemy.orm import Session
from app import models
from ..schemas import judges_schemas


def create_judge(db: Session, judge: judges_schemas.JudgeCreate):
    random_password = generate_random_password()
    hashed_password = hash_password(random_password)
    db_judge = models.Judge(**judge.model_dump(), password=hashed_password)
    db.add(db_judge)
    db.commit()
    db.refresh(db_judge)
    return db_judge, random_password

def get_all_judges(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Judge).offset(skip).limit(limit).all()

def get_judge(db: Session, judge_id: int):
    return db.query(models.Judge).filter(models.Judge.id == judge_id).first()

def delete_judge(db: Session, judge_id: int):
    judge = db.query(models.Judge).filter(models.Judge.id == judge_id).first()
    if judge:
        db.delete(judge)
        db.commit()
        return judge
    
def update_judge(db: Session, judge_id: int, updated_judge: judges_schemas.JudgeCreate):
    existing_judge = db.query(models.Judge).filter(models.Judge.id == judge_id).first()

    if existing_judge:
        for key, value in updated_judge.model_dump().items():
            setattr(existing_judge, key, value)

        db.commit()
        db.refresh(existing_judge)
        return existing_judge