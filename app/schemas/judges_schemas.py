from pydantic import BaseModel


class JudgeBase(BaseModel):
    name: str
    email: str

class JudgeCreate(JudgeBase):
    pass


class Judge(JudgeBase):
    id: int

    class Config:
        from_attributes = True

class JudgeWithPassword(JudgeBase):
    id : int 
    password : str