import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc4Agg(Base):
    """Maps to mc4_agg table in invitrodb databases."""

    __tablename__ = 'mc4_agg'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    aeid = Column(BIGINT, nullable=False)
    m0id = Column(BIGINT, nullable=False)
    m1id = Column(BIGINT, nullable=False)
    m2id = Column(BIGINT, nullable=False)
    m3id = Column(BIGINT, nullable=False)
    m4id = Column(BIGINT, nullable=False)