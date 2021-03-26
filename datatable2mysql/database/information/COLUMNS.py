import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Columns(Base):
    """Maps to COLUMNS table in information databases."""

    __tablename__ = 'COLUMNS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_CATALOG = Column(String(512), nullable=False)
    TABLE_SCHEMA = Column(String(64), nullable=False)
    TABLE_NAME = Column(String(64), nullable=False)
    COLUMN_NAME = Column(String(64), nullable=False)
    ORDINAL_POSITION = Column(BIGINT, nullable=False, defualt=0)
    COLUMN_DEFAULT = Column(LONGTEXT)
    IS_NULLABLE = Column(String(3), nullable=False)
    DATA_TYPE = Column(String(64), nullable=False)
    CHARACTER_MAXIMUM_LENGTH = Column(BIGINT)
    CHARACTER_OCTET_LENGTH = Column(BIGINT)
    NUMERIC_PRECISION = Column(BIGINT)
    NUMERIC_SCALE = Column(BIGINT)
    DATETIME_PRECISION = Column(BIGINT)
    CHARACTER_SET_NAME = Column(String(32))
    COLLATION_NAME = Column(String(32))
    COLUMN_TYPE = Column(LONGTEXT, nullable=False)
    COLUMN_KEY = Column(String(3), nullable=False)
    EXTRA = Column(String(30), nullable=False)
    PRIVILEGES = Column(String(80), nullable=False)
    COLUMN_COMMENT = Column(String(1024), nullable=False)
    GENERATION_EXPRESSION = Column(LONGTEXT, nullable=False)