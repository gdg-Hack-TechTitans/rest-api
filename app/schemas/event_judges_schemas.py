from pydantic import BaseModel


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
