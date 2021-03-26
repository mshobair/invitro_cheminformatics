import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Activities(Base):
    """Maps to activities table in chemprop databases."""

    __tablename__ = 'activities'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    action = Column(String)
    trackable_id = Column(Integer)
    trackable_type = Column(String)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)