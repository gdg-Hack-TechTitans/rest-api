from pydantic import BaseModel


class LostObjectBase(BaseModel):
    img_link : str
    id_event : int
    status : bool

class LostObjectCreate(LostObjectBase):
    pass 

class LostObject(LostObjectCreate): 
    pass 
