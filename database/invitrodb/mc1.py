import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP


from database.base import Base


class Mc1(Base):
    """Maps to mc1 table in invitrodb databases."""

    __tablename__ = 'mc1'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m1id = Column(BIGINT, nullable=True, primary_key=True)
    m0id = Column(BIGINT)
    acid = Column(BIGINT)
    cndx = Column(Integer)
    repi = Column(Integer)

    modified_by = Column(String(255))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.datetime.now, nullable=False)