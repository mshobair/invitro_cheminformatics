import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Statistics(Base):
    """Maps to STATISTICS table in information databases."""

    __tablename__ = 'STATISTICS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_CATALOG = Column(String, nullable=False)
    # TABLE_SCHEMA =
    TABLE_NAME = Column(String, nullable=False)
    NON_UNIQUE = Column(BIGINT, nullable=False, default=0)
    INDEX_SCHEMA = Column(String, nullable=False)
    INDEX_NAME = Column(String, nullable=False)
    SEQ_IN_INDEX = Column(BIGINT, nullable=False, default=0)
    COLUMN_NAME = Column(String, nullable=False)
    COLLATION = Column(String)
    CARDINALITY = Column(BIGINT)
    SUB_PART = Column(BIGINT)
    PACKED = Column(String)
    NULLABLE = Column(String, nullable=False)
    INDEX_TYPE = Column(String, nullable=False)
    COMMENT = Column(String)
    INDEX_COMMENT = Column(String, nullable=False)