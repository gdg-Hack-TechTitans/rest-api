from pydantic import BaseModel

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

class MentorWithPassword(MentorBase):
    id : int 
    password : str