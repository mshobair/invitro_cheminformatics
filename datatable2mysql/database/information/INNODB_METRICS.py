import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbMetrics(Base):
    """Maps to INNODB_METRICS table in information databases."""

    __tablename__ = 'INNODB_METRICS'
    __table_args__ = {'schema': Schemas.information_schema}

    NAME = Column(String, nullable=False)
    SUBSYSTEM = Column(String, nullable=False)
    COUNT = Column(BIGINT, nullable=False, default=0)
    MAX_COUNT = Column(BIGINT)
    MIN_COUNT = Column(BIGINT)
    AVG_COUNT = Column(DOUBLE)
    COUNT_RESET = Column(BIGINT, nullable=False, default=0)
    MAX_COUNT_RESET = Column(BIGINT)
    MIN_COUNT_RESET = Column(BIGINT)
    AVG_COUNT_RESET = Column(DOUBLE)
    TIME_ENABLED = Column(DateTime)
    TIME_DISABLED = Column(DateTime)
    TIME_ELAPSED = Column(BIGINT)
    TIME_RESET = Column(DateTime)
    STATUS = Column(String, nullable=False)
    TYPE = Column(String, nullable=False)
    COMMENT = Column(String, nullable=False)