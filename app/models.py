from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(String, default="open")  # open, in_progress, resolved, closed
    source = Column(String, nullable=False)  # operator, monitoring, partner
    created_at = Column(DateTime(timezone=True), server_default=func.now())