from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import mentors_schemas
from ..crud import mentors_crud


mentor_router = APIRouter()

@mentor_router.post("/v1/mentors/", response_model=mentors_schemas.MentorWithPassword, status_code=201)
def create_mentor(mentor: mentors_schemas.MentorCreate, db: Session = Depends(get_db)):
    created_mentor, random_password = mentors_crud.create_mentor(db=db, mentor=mentor)

    # Instead of returning a dictionary, return an instance of MentorWithPassword
    response_mentor = mentors_schemas.MentorWithPassword(
        id=created_mentor.id,
        name=created_mentor.name,
        email=created_mentor.email,
        role=created_mentor.role,
        password=random_password
    )

    return response_mentor

@mentor_router.get("/v1/mentors/", response_model=list[mentors_schemas.Mentor])
def get_mentors(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return mentors_crud.get_all_mentors(db, skip, limit)


@mentor_router.get("/v1/mentors/{mentor_id}/", response_model=mentors_schemas.Mentor)
def get_event(mentor_id: int , db: Session = Depends(get_db)):
    db_mentor = mentors_crud.get_mentor(db,mentor_id=mentor_id)
    print(db_mentor)
    if db_mentor is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_mentor

@mentor_router.delete("/v1/mentors/{mentor_id}/", response_model=mentors_schemas.Mentor)
def delete_event(mentor_id: int , db: Session = Depends(get_db)):
    return mentors_crud.delete_mentor(db, mentor_id=mentor_id)

@mentor_router.put("/v1/mentors/{mentor_id}/", response_model=mentors_schemas.Mentor)
def update_event(mentor_id: int ,mentor: mentors_schemas.MentorCreate, db: Session = Depends(get_db)):
    return mentors_crud.update_mentor(db, mentor_id=mentor_id, updated_mentor=mentor)



'''




@mentor_router.put("/v1/mentors/{mentor_id}/", response_model=mentors_crud.Mentor)
def update_event(mentor_id: int ,event: mentors_crud.EventCreate, db: Session = Depends(get_db)):
    return mentors_crud.update_event(db, mentor_id=mentor_id, event=event)
'''