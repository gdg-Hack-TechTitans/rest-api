from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import events_schemas
from ..crud import events_crud


event_router = APIRouter()

@event_router.post("/v1/events/", response_model=events_schemas.Event, status_code=201)
def create_event(event: events_schemas.EventCreate, db: Session = Depends(get_db)):
    return events_crud.create_event(db=db, event = event)

@event_router.get("/v1/events/", response_model=list[events_schemas.Event])
def get_events(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return events_crud.get_events(db, skip, limit)

@event_router.get("/v1/events/{event_id}/", response_model=events_schemas.Event)
def get_event(event_id: int , db: Session = Depends(get_db)):
    db_event= events_crud.get_event(db,event_id=event_id)
    print(db_event)
    if db_event is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_event

@event_router.delete("/v1/events/{event_id}/", response_model=events_schemas.Event)
def delete_event(event_id: int , db: Session = Depends(get_db)):
    return events_crud.delete_event(db, event_id=event_id)

@event_router.put("/v1/events/{event_id}/", response_model=events_schemas.Event)
def update_event(event_id: int ,event: events_schemas.EventCreate, db: Session = Depends(get_db)):
    return events_crud.update_event(db, event_id=event_id, event=event)
