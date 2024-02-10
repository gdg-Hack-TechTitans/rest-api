from pydantic import BaseModel


class EventCriteriaBase(BaseModel):
    id_event: int
    name_criteria: str
    score: int

class EventCriteriaCreate(EventCriteriaBase):
    pass

class EventCriteria(EventCriteriaBase):
    pass
