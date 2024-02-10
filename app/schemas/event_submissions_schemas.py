from pydantic import BaseModel

class EventSubmissionBase(BaseModel):
    id_event: int
    id_team: int
    id_field: str
    submission: str

class EventSubmissionCreate(EventSubmissionBase):
    pass

class EventSubmission(EventSubmissionBase):
    pass

