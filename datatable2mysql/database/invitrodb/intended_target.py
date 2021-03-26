import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class IntendedTarget(Base):
    """Maps to intended_target table in invitrodb databases."""

    __tablename__ = 'intended_target'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    aeid = Column(Integer)
    target_id = Column(Integer)
    source = Column(String(255))