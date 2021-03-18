import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbBuferPage(Base):
    """Maps to INNODB_BUFFER_PAGE table in information databases."""

    __tablename__ = 'INNODB_BUFFER_PAGE'
    __table_args__ = {'schema': Schemas.information_schema}

    POOL_ID = Column(BIGINT, nullable=False, default=0)
    BLOCK_ID = Column(BIGINT, nullable=False, default=0)
    SPACE = Column(BIGINT, nullable=False, default=0)
    PAGE_NUMBER = Column(BIGINT, nullable=False, default=0)
    PAGE_TYPE = Column(String)
    FLUSH_TYPE = Column(BIGINT, nullable=False, default=0)
    FIX_COUNT = Column(BIGINT, nullable=False, default=0)
    IS_HASHED = Column(String)
    NEWEST_MODIFICATION = Column(BIGINT, nullable=False, default=0)
    OLDEST_MODIFICATION = Column(BIGINT, nullable=False, default=0)
    ACCESS_TIME = Column(BIGINT, nullable=False, default=0)
    TABLE_NAME = Column(String)
    INDEX_NAME = Column(String)
    NUMBER_RECORDS = Column(BIGINT, nullable=False, default=0)
    DATA_SIZE = Column(BIGINT, nullable=False, default=0)
    COMPRESSED_SIZE = Column(BIGINT, nullable=False, default=0)
    PAGE_STATE = Column(String)
    IO_FIX = Column(String)
    IS_OLD = Column(String)
    FREE_PAGE_CLOCK = Column(BIGINT, nullable=False, default=0)