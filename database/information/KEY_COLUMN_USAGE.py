import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class KeyColumnUsage(Base):
    """Maps to KEY_COLUMN_USAGE table in information databases."""

    __tablename__ = 'KEY_COLUMN_USAGE'
    __table_args__ = {'schema': Schemas.information_schema}

    CONSTRAINT_CATALOG = Column(String, nullable=False)
    CONSTRAINT_SCHEMA = Column(String, nullable=False)
    CONSTRAINT_NAME = Column(String, nullable=False)
    TABLE_CATALOG = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False)
    COLUMN_NAME = Column(String, nullable=False)
    ORDINAL_POSITION = Column(BIGINT, nullable=False, default=0)
    POSITION_IN_UNIQUE_CONSTRAINT = Column(BIGINT)
    REFERENCED_TABLE_SCHEMA = Column(String)
    REFERENCED_TABLE_NAME = Column(String)
    REFERENCED_COLUMN_NAME = Column(String)