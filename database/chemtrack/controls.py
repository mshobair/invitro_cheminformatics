import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Controls(Base):
    """Maps to controls table in chemprop databases."""

    __tablename__ = 'controls'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer)
    source_substance_id = Column(Integer)
    controls = Column(Integer, default=0)
    identifier = Column(String)
    standard_replicate = Column(Integer, default=0)
    originally_found_replicate = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)