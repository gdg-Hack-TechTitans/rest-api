from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import speakers_schemas
from ..crud import speakers_crud


speaker_router = APIRouter()

@speaker_router.post("/v1/speakers/", response_model=speakers_schemas.SpeakerWithPassword, status_code=201)
def create_speaker(speaker: speakers_schemas.SpeakerCreate, db: Session = Depends(get_db)):
    created_speaker, random_password = speakers_crud.create_speaker(db=db, speaker=speaker)

    # Instead of returning a dictionary, return an instance of SpeakerWithPassword
    response_speaker = speakers_schemas.SpeakerWithPassword(
        id=created_speaker.id,
        name=created_speaker.name,
        email=created_speaker.email,
        password=random_password
    )

    return response_speaker

@speaker_router.get("/v1/speakers/", response_model=list[speakers_schemas.Speaker])
def get_speakers(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return speakers_crud.get_all_speakers(db, skip, limit)


@speaker_router.get("/v1/speakers/{speaker_id}/", response_model=speakers_schemas.Speaker)
def get_event(speaker_id: int , db: Session = Depends(get_db)):
    db_speaker = speakers_crud.get_speaker(db,speaker_id=speaker_id)
    print(db_speaker)
    if db_speaker is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_speaker

@speaker_router.delete("/v1/speakers/{speaker_id}/", response_model=speakers_schemas.Speaker)
def delete_event(speaker_id: int , db: Session = Depends(get_db)):
    return speakers_crud.delete_speaker(db, speaker_id=speaker_id)

@speaker_router.put("/v1/speakers/{speaker_id}/", response_model=speakers_schemas.Speaker)
def update_event(speaker_id: int ,speaker: speakers_schemas.SpeakerCreate, db: Session = Depends(get_db)):
    return speakers_crud.update_speaker(db, speaker_id=speaker_id, updated_speaker=speaker)



'''




@speaker_router.put("/v1/speakers/{speaker_id}/", response_model=speakers_crud.Speaker)
def update_event(speaker_id: int ,event: speakers_crud.EventCreate, db: Session = Depends(get_db)):
    return speakers_crud.update_event(db, speaker_id=speaker_id, event=event)
'''