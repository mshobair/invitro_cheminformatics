import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Partitions(Base):
    """Maps to PARTITIONS table in information databases."""

    __tablename__ = 'PARTITIONS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_CATALOG = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False)
    PARTITION_NAME = Column(String)
    SUBPARTITION_NAME = Column(String)
    PARTITION_ORDINAL_POSITION = Column(BIGINT)
    SUBPARTITION_ORDINAL_POSITION = Column(BIGINT)
    PARTITION_METHOD = Column(String)
    SUBPARTITION_METHOD = Column(String)
    PARTITION_EXPRESSION = Column(LONGTEXT)
    SUBPARTITION_EXPRESSION = Column(LONGTEXT)
    PARTITION_DESCRIPTION = Column(LONGTEXT)
    TABLE_ROWS = Column(BIGINT, nullable=False, default=0)
    AVG_ROW_LENGTH = Column(BIGINT, nullable=False, default=0)
    DATA_LENGTH = Column(BIGINT, nullable=False, default=0)
    MAX_DATA_LENGTH = Column(BIGINT)
    INDEX_LENGTH = Column(BIGINT, nullable=False, default=0)
    DATA_FREE = Column(BIGINT, nullable=False, default=0)
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CHECK_TIME = Column(DateTime)
    CHECKSUM = Column(BIGINT)
    PARTITION_COMMENT = Column(String, nullable=False)
    NODEGROUP = Column(String, nullable=False)
    TABLESPACE_NAME = Column(String)