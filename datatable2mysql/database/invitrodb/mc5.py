import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc5(Base):
    """Maps to mc5 table in invitrodb databases."""

    __tablename__ = 'mc5'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m5id = Column(BIGINT, nullable=False, primary_key=True)
    m4id = Column(BIGINT, nullable=False)
    aeid = Column(BIGINT, nullable=False)
    modl = Column(String(4), default='cnst')
    hitc = Column(TINYINT, default=0)
    fitc = Column(TINYINT, default=1)
    coff = Column(DOUBLE)
    actp = Column(DOUBLE)
    modl_er = Column(DOUBLE)
    modl_tp = Column(DOUBLE)
    modl_ga = Column(DOUBLE)
    modl_gw = Column(DOUBLE)
    modl_la = Column(DOUBLE)
    modl_lw = Column(DOUBLE)
    modl_prob = Column(DOUBLE)
    modl_rmse = Column(DOUBLE)
    modl_acc = Column(DOUBLE)
    modl_acb = Column(DOUBLE)
    modl_ac10 = Column(DOUBLE)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)