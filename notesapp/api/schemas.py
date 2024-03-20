from datetime import datetime
from pydantic import BaseModel


class GetNote(BaseModel):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UpdateNote(BaseModel):
    text: str
