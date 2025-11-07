from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncidentBase(BaseModel):
    description: str
    status: str = "open"
    source: str


class IncidentCreate(IncidentBase):
    pass


class IncidentStatusUpdate(BaseModel):
    status: str


class Incident(IncidentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True