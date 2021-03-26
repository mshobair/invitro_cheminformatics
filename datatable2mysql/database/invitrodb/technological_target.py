import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class TechnologicalTarget(Base):
    """Maps to technological_target table in invitrodb databases."""

    __tablename__ = 'technological_target'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    acid = Column(Integer)
    target_id = Column(Integer)
    source = Column(String(255))