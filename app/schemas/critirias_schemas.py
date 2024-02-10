from pydantic import BaseModel

class CriteriaBase(BaseModel):
    name: str
    name_field: str

class CriteriaCreate(CriteriaBase):
    pass

class Criteria(CriteriaBase):
    pass
