import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sample(Base):
    """Maps to sample table in invitrodb databases."""

    __tablename__ = 'sample'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    spid = Column(String(50), nullable=False, primary_key=True)

    chid = Column(Integer)
    stkc = Column(DOUBLE)
    stkc_unit = Column(String(50))
    tested_conc_unit = Column(String(50))
    spid_legacy = Column(String(50))