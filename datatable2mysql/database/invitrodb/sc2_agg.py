import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base

class Sc2Agg(Base):
    """Maps to sc2_agg table in invitrodb databases."""

    __tablename__ = 'sc2_agg'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    aeid = Column(BIGINT, nullable=False)
    s0id = Column(BIGINT, nullable=False)
    s1id = Column(BIGINT, nullable=False)
    s2id = Column(BIGINT, nullable=False)
