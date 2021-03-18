import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysTablestats(Base):
    """Maps to INNODB_SYS_TABLESTATS table in information databases."""

    __tablename__ = 'INNODB_SYS_TABLESTATS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    STATS_INITIALIZED = Column(String, nullable=False)
    NUM_ROWS = Column(BIGINT, nullable=False, default=0)
    CLUST_INDEX_SIZE = Column(BIGINT, nullable=False, default=0)
    OTHER_INDEX_SIZE = Column(BIGINT, nullable=False, default=0)
    MODIFIED_COUNTER = Column(BIGINT, nullable=False, default=0)
    AUTOINC = Column(BIGINT, nullable=False, default=0)
    REF_COUNT = Column(Integer, nullable=False, default=0)