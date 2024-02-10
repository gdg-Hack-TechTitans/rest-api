from pydantic import BaseModel

class SpeakerBase(BaseModel):
    name: str
    email: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int

    class Config:
        from_attributes = True

class SpeakerWithPassword(SpeakerBase):
    id : int 
    password : str