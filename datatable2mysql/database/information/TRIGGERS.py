import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Triggers(Base):
    """Maps to TRIGGERS table in information databases."""

    __tablename__ = 'TRIGGERS'
    __table_args__ = {'schema': Schemas.information_schema}

    TRIGGER_CATALOG = Column(String, nullable=False)
    TRIGGER_SCHEMA = Column(String, nullable=False)
    TRIGGER_NAME = Column(String, nullable=False)
    EVENT_MANIPULATION = Column(String, nullable=False)
    EVENT_OBJECT_CATALOG = Column(String, nullable=False)
    EVENT_OBJECT_SCHEMA = Column(String, nullable=False)
    EVENT_OBJECT_TABLE = Column(String, nullable=False)
    ACTION_ORDER = Column(BIGINT, nullable=False, default=0)
    ACTION_CONDITION = Column(LONGTEXT)
    ACTION_STATEMENT = Column(LONGTEXT, nullable=False)
    ACTION_ORIENTATION = Column(String, nullable=False)
    ACTION_TIMING = Column(String, nullable=False)
    ACTION_REFERENCE_OLD_TABLE = Column(String)
    ACTION_REFERENCE_NEW_TABLE = Column(String)
    ACTION_REFERENCE_OLD_ROW = Column(String, nullable=False)
    ACTION_REFERENCE_NEW_ROW = Column(String, nullable=False)
    CREATED = Column(DateTime)
    SQL_MODE = Column(String, nullable=False)
    DEFINER = Column(String, nullable=False)
    CHARACTER_SET_CLIENT = Column(String, nullable=False)
    COLLATION_CONNECTION = Column(String, nullable=False)
    DATABASE_COLLATION = Column(String, nullable=False)