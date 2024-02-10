from pydantic import BaseModel
from typing import Optional


class ParticipantBase(BaseModel):
    name: str
    email: str
    linkedin: Optional[str]
    is_public: bool

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int

    class Config:
        from_attributes = True
