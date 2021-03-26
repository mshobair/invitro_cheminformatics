import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class SpidMap(Base):
    """Maps to spid_map table in invitrodb databases."""

    __tablename__ = 'spid_map'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    spid_map_id = Column(Integer, nullable=False, primary_key=True)
    spid_source = Column(String(100))
    type = Column(String(2))
    srcf = Column(String(500))
    asid = Column(Integer)
    asnm = Column(String(100))
    aid = Column(Integer, nullable=False)
    anm = Column(String(100), nullable=False)
    maxc_before_correction = Column(DOUBLE)
    maxc_after_correction = Column(DOUBLE)
    tested_conc_unit = Column(String(10), nullable=False)
    npts = Column(DOUBLE)
    spid = Column(String(50))
    conc_correction_factor = Column(DOUBLE)
    df_calc = Column(DOUBLE, nullable=False)
    diff_log_plated_conc_insource = Column(DOUBLE)
    plate_mapping_confidence = Column(String(45))
    stkc = Column(DOUBLE)
    stkc_unit = Column(DOUBLE)
