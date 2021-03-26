import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class PiRelationships(Base):
    """Maps to pi_relationships table in chemprop databases."""

    __tablename__ = 'pi_relationships'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    pi_id = Column(Integer)
    user_id = Column(Integer)
    user_type = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)