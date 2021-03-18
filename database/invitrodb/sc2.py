import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sc2(Base):
    """Maps to sc2 table in invitrodb databases."""

    __tablename__ = 'sc2'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    s2id = Column(BIGINT, nullable=False, primary_key=True)
    aeid = Column( Integer, nullable=False)
    spid = Column(String(50), nullable=False )
    bmad = Column(DOUBLE, nullable=False)
    max_med = Column(DOUBLE, nullable=False)
    coff = Column(DOUBLE, nullable=False)
    hitc = Column(DOUBLE, nullable=False)
    tmpi = Column(Integer, nullable=False)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)