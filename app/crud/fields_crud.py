from sqlalchemy.orm import Session
from ..schemas import fields_schemas
from app import models

def get_field(db: Session, field_name: str):
    return db.query(models.Field).filter(models.Field.name == field_name).first()

def get_fields(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Field).offset(skip).limit(limit).all()

def create_field(db: Session, field: fields_schemas.FieldCreate):
    db_field = models.Field(**field.model_dump())
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

def delete_field(db: Session, field_name: str):
    db_field = db.query(models.Field).filter(models.Field.name == field_name).first()
    if db_field:
        db.delete(db_field)
        db.commit()
    return db_field

def update_field(db: Session, field_name: str, field: fields_schemas.FieldCreate):
    db_field = db.query(models.Field).filter(models.Field.name == field_name).first()
    if db_field:
        for key, value in field.model_dump().items():
            setattr(db_field, key, value)
        db.commit()
        db.refresh(db_field)
    return db_field
