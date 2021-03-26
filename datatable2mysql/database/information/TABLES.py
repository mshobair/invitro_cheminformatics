import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Tables(Base):
    """Maps to TABLES table in information databases."""

    __tablename__ = 'TABLES'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_CATALOG = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False, primary_key=True)
    TABLE_TYPE = Column(String, nullable=False)
    ENGINE = Column(String)
    VERSION = Column(BIGINT)
    ROW_FORMAT = Column(String)
    TABLE_ROWS = Column(BIGINT)
    AVG_ROW_LENGTH = Column(BIGINT)
    DATA_LENGTH = Column(BIGINT)
    MAX_DATA_LENGTH = Column(BIGINT)
    INDEX_LENGTH = Column(BIGINT)
    DATA_FREE = Column(BIGINT)
    AUTO_INCREMENT = Column(BIGINT)
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CHECK_TIME = Column(DateTime)
    TABLE_COLLATION = Column(String)
    CHECKSUM = Column(BIGINT)
    CREATE_OPTIONS = Column(String)
    TABLE_COMMENT = Column(String)