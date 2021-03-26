import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP

from database.base import Base


class Mc0(Base):
    """Maps to mc0 table in invitrodb databases."""

    __tablename__ = 'mc0'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m0id = Column(BIGINT, nullable=False, primary_key=True)
    acid = Column(BIGINT, nullable=False)
    spid = Column(String, nullable=False)
    apid = Column(String(100))
    rowi = Column(Integer)
    coli = Column(Integer)
    wllt = Column(String(1), nullable=False)
    wllq = Column(SMALLINT, nullable=False)
    conc = Column(DOUBLE)
    rval = Column(DOUBLE)
    srcf = Column(String(255), nullable=False)
    modified_by = Column(String(100))
    created_date = Column(TIMESTAMP, default=datetime.datetime.now, nullable=False)
    modified_date = Column(TIMESTAMP, default=datetime.datetime.now, nullable=False)