import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Events(Base):
    """Maps to EVENTS table in information databases."""

    __tablename__ = 'EVENTS'
    __table_args__ = {'schema': Schemas.information_schema}

    EVENT_CATALOG = Column(String(64), nullable=False)
    EVENT_SCHEMA = Column(String(64), nullable=False)
    EVENT_NAME = Column(String(64), nullable=False)
    DEFINER = Column(String(93), nullable=False)
    TIME_ZONE = Column(String(64), nullable=False)
    EVENT_BODY = Column(String(8), nullable=False)
    EVENT_DEFINITION = Column(LONGTEXT, nullable=False)
    EVENT_TYPE = Column(String(9), nullable=False)
    EXECUTE_AT = Column(DateTime)
    INTERVAL_VALUE = Column(String(256))
    INTERVAL_FIELD = Column(String(18))
    SQL_MODE = Column(String(8192), nullable=False)
    STARTS = Column(DateTime)
    ENDS = Column(DateTime)
    STATUS = Column(String(18), nullable=False)
    ON_COMPLETION = Column(String, nullable=False)
    CREATED = Column(DateTime, nullable=False)
    LAST_ALTERED = Column(DateTime, nullable=False)
    LAST_EXECUTED = Column(DateTime)
    EVENT_COMMENT = Column(String(64), nullable=False)
    ORIGINATOR = Column(BIGINT, nullable=False, default=0)
    CHARACTER_SET_CLIENT = Column(String(32), nullable=False)
    COLLATION_CONNECTION = Column(String(32), nullable=False)
    DATABASE_COLLATION = Column(String(32), nullable=False)