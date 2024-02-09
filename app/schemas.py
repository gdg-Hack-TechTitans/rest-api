'''
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


##########################################
        
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True

##########################################

class EventBase(BaseModel):
    name : str
    type : str
    date : str
    description : str
    drive : str
    thumbnail : str

class Event(EventBase):
    id : int

class EventCreate(EventBase):
    pass

##########################################

class TeamBase(BaseModel):
    name : str

class Team(TeamBase):
    id : int

class TeamCreate(TeamBase):
    pass 

##########################################

class EventTeamBase(BaseModel):
    name : str

class Team(TeamBase):
    id : int

class TeamCreate(TeamBase):
    pass 
'''

from typing import Optional
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

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        from_attributes = True

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

class MentorBase(BaseModel):
    name: str
    email: str
    role: str

class MentorCreate(MentorBase):
    pass

class Mentor(MentorBase):
    id: int

    class Config:
        from_attributes = True

class SpeakerBase(BaseModel):
    name: str
    email: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int

    class Config:
        from_attributes = True

class FieldBase(BaseModel):
    name: str

class FieldCreate(FieldBase):
    pass

class Field(FieldBase):
    pass

class CriteriaBase(BaseModel):
    name: str
    name_field: str

class CriteriaCreate(CriteriaBase):
    pass

class Criteria(CriteriaBase):
    pass

class EventCriteriaBase(BaseModel):
    id_event: int
    name_criteria: str
    score: int

class EventCriteriaCreate(EventCriteriaBase):
    pass

class EventCriteria(EventCriteriaBase):
    pass

class EventSubmissionBase(BaseModel):
    id_event: int
    id_team: int
    id_field: str
    submission: str

class EventSubmissionCreate(EventSubmissionBase):
    pass

class EventSubmission(EventSubmissionBase):
    pass

class JudgeBase(BaseModel):
    name: str
    email: str

class JudgeCreate(JudgeBase):
    password: str


class Judge(JudgeBase):
    id: int

    class Config:
        from_attributes = True

class EventJudgeBase(BaseModel):
    id_judge: int
    id_event: int
    id_team: int
    name_criteria: str
    judgment: str
    role: str

class EventJudgeCreate(EventJudgeBase):
    pass

class EventJudge(EventJudgeBase):
    pass

class LostObjectBase(BaseModel):
    img_link : str
    id_event : int
    status : bool

class LostObjectCreate(LostObjectBase):
    pass 

class LostObject(LostObjectCreate): 
    pass 