from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import fields_schemas
from ..crud import fields_crud


field_router = APIRouter()

@field_router.post("/v1/fields/", response_model=fields_schemas.Field, status_code=201)
def create_field(field: fields_schemas.FieldCreate, db: Session = Depends(get_db)):
    return fields_crud.create_field(db=db, field= field)

@field_router.get("/v1/fields/", response_model=list[fields_schemas.Field])
def get_fields(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return fields_crud.get_fields(db, skip, limit)

@field_router.get("/v1/fields/{field_name}/", response_model=fields_schemas.Field)
def get_field(field_name: str , db: Session = Depends(get_db)):
    db_field= fields_crud.get_field(db,field_name=field_name)
    print(db_field)
    if db_field is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_field

@field_router.delete("/v1/fields/{field_name}/", response_model=fields_schemas.Field)
def delete_field(field_name: str , db: Session = Depends(get_db)):
    return fields_crud.delete_field(db, field_name=field_name)

@field_router.put("/v1/fields/{field_name}/", response_model=fields_schemas.Field)
def update_field(field_name: str ,field: fields_schemas.FieldCreate, db: Session = Depends(get_db)):
    return fields_crud.update_field(db, field_name=field_name, field=field)
