import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP


from database.base import Base


class Mc3(Base):
    """Maps to mc3 table in invitrodb databases."""

    __tablename__ = 'mc3'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m3id = Column(BIGINT, nullable=False, primary_key=True)
    aeid = Column(BIGINT)
    m0id = Column(BIGINT)
    acid = Column(BIGINT)
    m1id = Column(BIGINT)
    m2id = Column(BIGINT)
    bval = Column(DOUBLE)
    pval = Column(DOUBLE)
    logc = Column(DOUBLE)
    resp = Column(DOUBLE)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)