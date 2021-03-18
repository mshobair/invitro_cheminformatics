import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sc0(Base):
    """Maps to sc0 table in invitrodb databases."""

    __tablename__ = 'sc0'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    s0id = Column(BIGINT, nullable=False, primary_key=True)
    acid = Column(BIGINT, nullable=False)
    spid = Column(String(50), nullable=False)
    apid = Column(String(100))
    rowi = Column(Integer)
    coli = Column(Integer)
    wllt = Column(String(1), nullable=False)
    wllq = Column(SMALLINT, nullable=False)
    conc = Column(DOUBLE)
    rval = Column(DOUBLE)
    srcf = Column(String(255), nullable=False)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)