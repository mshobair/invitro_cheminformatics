import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Files(Base):
    """Maps to FILES table in information databases."""

    __tablename__ = 'FILES'
    __table_args__ = {'schema': Schemas.information_schema}

    FILE_ID = Column(BIGINT, nullable=False, default=0)
    FILE_NAME = Column(String(4000))
    FILE_TYPE = Column(String(20))
    TABLESPACE_NAME = Column(String)
    TABLE_CATALOG = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String)
    TABLE_NAME = Column(String)
    LOGFILE_GROUP_NAME = Column(String)
    LOGFILE_GROUP_NUMBER = Column(BIGINT)
    ENGINE = Column(String, nullable=False)
    FULLTEXT_KEYS = Column(String)
    DELETED_ROWS = Column(BIGINT)
    UPDATE_COUNT = Column(BIGINT)
    FREE_EXTENTS = Column(BIGINT)
    TOTAL_EXTENTS = Column(BIGINT)
    EXTENT_SIZE = Column(BIGINT, nullable=False, default=0)
    INITIAL_SIZE = Column(BIGINT)
    MAXIMUM_SIZE = Column(BIGINT)
    AUTOEXTEND_SIZE = Column(BIGINT)
    CREATION_TIME = Column(datetime)
    LAST_UPDATE_TIME = Column(datetime)
    LAST_ACCESS_TIME = Column(datetime)
    RECOVER_TIME = Column(BIGINT)
    TRANSACTION_COUNTER = Column(BIGINT)
    VERSION = Column(BIGINT)
    ROW_FORMAT = Column(BIGINT)
    TABLE_ROWS = Column(BIGINT)
    AVG_ROW_LENGTH = Column(BIGINT)
    DATA_LENGTH = Column(BIGINT)
    MAX_DATA_LENGTH = Column(BIGINT)
    INDEX_LENGTH = Column(BIGINT)
    DATA_FREE = Column(BIGINT)
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CHECK_TIME = Column(DateTime)
    CHECKSUM = Column(BIGINT)
    STATUS = Column(String, nullable=False)
    EXTRA = Column(String)