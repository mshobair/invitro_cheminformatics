import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbBufferPoolStats(Base):
    """Maps to INNODB_BUFFER_POOL_STATS table in information databases."""

    __tablename__ = 'INNODB_BUFFER_POOL_STATS'
    __table_args__ = {'schema': Schemas.information_schema}

    POOL_ID = Column(BIGINT, nullable=False, default=0)
    POOL_SIZE = Column(BIGINT, nullable=False, default=0)
    FREE_BUFFERS = Column(BIGINT, nullable=False, default=0)
    DATABASE_PAGES = Column(BIGINT, nullable=False, default=0)
    OLD_DATABASE_PAGES = Column(BIGINT, nullable=False, default=0)
    MODIFIED_DATABASE_PAGES = Column(BIGINT, nullable=False, default=0)
    PENDING_DECOMPRESS = Column(BIGINT, nullable=False, default=0)
    PENDING_READS = Column(BIGINT, nullable=False, default=0)
    PENDING_FLUSH_LRU = Column(BIGINT, nullable=False, default=0)
    PENDING_FLUSH_LIST = Column(BIGINT, nullable=False, default=0)
    PAGES_MADE_YOUNG = Column(BIGINT, nullable=False, default=0)
    PAGES_NOT_MADE_YOUNG = Column(BIGINT, nullable=False, default=0)
    PAGES_MADE_YOUNG_RATE = Column(DOUBLE, nullable=False, default=0)
    PAGES_MADE_NOT_YOUNG_RATE = Column(DOUBLE, nullable=False, default=0)
    NUMBER_PAGES_READ = Column(BIGINT, nullable=False, default=0)
    NUMBER_PAGES_CREATED = Column(BIGINT, nullable=False, default=0)
    NUMBER_PAGES_WRITTEN = Column(BIGINT, nullable=False, default=0)
    PAGES_READ_RATE = Column(DOUBLE, nullable=False, default=0)
    PAGES_CREATE_RATE = Column(DOUBLE, nullable=False, default=0)
    PAGES_WRITTEN_RATE = Column(DOUBLE, nullable=False, default=0)
    NUMBER_PAGES_GET = Column(BIGINT, nullable=False, default=0)
    HIT_RATE = Column(BIGINT, nullable=False, default=0)
    YOUNG_MAKE_PER_THOUSAND_GET = Column(BIGINT, nullable=False, default=0)
    NOT_YOUNG_PER_THOUSAND_GET = Column(BIGINT, nullable=False, default=0)
    NUMBER_PAGES_READ_AHEAD = Column(BIGINT, nullable=False, default=0)
    NUMBER_READ_AHEAD_EVICTED = Column(BIGINT, nullable=False, default=0)
    READ_AHEAD_RATE = Column(DOUBLE, nullable=False, default=0)
    READ_AHEAD_EVICTED_RATE = Column(DOUBLE, nullable=False, default=0)
    LRU_IO_TOTAL = Column(BIGINT, nullable=False, default=0)
    LRU_IO_CURRENT = Column(BIGINT, nullable=False, default=0)
    UNCOMPRESS_TOTAL = Column(BIGINT, nullable=False, default=0)
    UNCOMPRESS_CURRENT = Column(BIGINT, nullable=False, default=0)