from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    name: str
    type: str
    date: date
    description: str
    drive: str
    thumbnail: str

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True