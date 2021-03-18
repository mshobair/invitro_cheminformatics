import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Parameters(Base):
    """Maps to parameters table in chemprop databases."""

    __tablename__ = "parameters"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))
    description = Column(String(255))
    standard_unit = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
