import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sc1(Base):
    """Maps to sc1 table in invitrodb databases."""

    __tablename__ = 'sc1'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    s1id = Column(BIGINT, nullable=False, primary_key=True)
    s0id = Column(Integer, nullable=False)
    acid = Column(Integer, nullable=False)
    aeid = Column(Integer, nullable=False)
    logc = Column(DOUBLE)
    bval = Column(DOUBLE)
    pval = Column(DOUBLE)
    resp = Column(DOUBLE, nullable=False)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)