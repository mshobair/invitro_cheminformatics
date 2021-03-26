import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, DECIMAL

from database.base import Base


class Profiling(Base):
    """Maps to PROFILING table in information databases."""

    __tablename__ = 'PROFILING'
    __table_args__ = {'schema': Schemas.information_schema}

    QUERY_ID = Column(Integer, nullable=False, default=0)
    SEQ = Column(Integer, nullable=False, default=0)
    STATE = Column(String, nullable=False)
    DURATION = Column(DECIMAL, nullable=False, default=0.000000)
    CPU_USER = Column(DECIMAL)
    CPU_SYSTEM = Column(DECIMAL)
    CONTEXT_VOLUNTARY = Column(Integer)
    CONTEXT_INVOLUNTARY = Column(Integer)
    BLOCK_OPS_IN = Column(Integer)
    BLOCK_OPS_OUT = Column(Integer)
    MESSAGES_SENT = Column(Integer)
    MESSAGES_RECEIVED = Column(Integer)
    PAGE_FAULTS_MAJOR = Column(Integer)
    PAGE_FAULTS_MINOR = Column(Integer)
    SWAPS = Column(Integer)
    SOURCE_FUNCTION = Column(String)
    SOURCE_FILE = Column(String)
    SOURCE_LINE = Column(Integer)