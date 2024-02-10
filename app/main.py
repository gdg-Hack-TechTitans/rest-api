from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
from .routers import (
    events,
    mentors,
    fields,
    speakers,
    judges, 
    teams
)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.event_router)
app.include_router(mentors.mentor_router)
app.include_router(fields.field_router)
app.include_router(speakers.speaker_router)
app.include_router(judges.judges_router)
app.include_router(judges.judges_router)
app.include_router(teams.team_router)
