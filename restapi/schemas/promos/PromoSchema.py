from pydantic import BaseModel

class PromoSchema(BaseModel):
    class Config:
        anystr_strip_whitespace = True

class PromoSearchByName(PromoSchema):
    id: str
    name: str
