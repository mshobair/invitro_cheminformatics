import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysIndexes(Base):
    """Maps to INNODB_SYS_INDEXES table in information databases."""

    __tablename__ = 'INNODB_SYS_INDEXES'
    __table_args__ = {'schema': Schemas.information_schema}

    INDEX_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    TYPE = Column(Integer, nullable=False, default=0)
    N_FIELDS = Column(Integer, nullable=False, default=0)
    PAGE_NO = Column(Integer, nullable=False, default=0)
    SPACE = Column(Integer, nullable=False, default=0)
    MERGE_THRESHOLD = Column(Integer, nullable=False, default=0)