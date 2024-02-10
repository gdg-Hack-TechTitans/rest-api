from pydantic import BaseModel

class FieldBase(BaseModel):
    name: str

class FieldCreate(FieldBase):
    pass

class Field(FieldBase):
    pass
