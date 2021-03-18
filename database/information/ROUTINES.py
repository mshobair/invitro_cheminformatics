import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Routines(Base):
    """Maps to ROUTINES table in information databases."""

    __tablename__ = 'ROUTINES'
    __table_args__ = {'schema': Schemas.information_schema}

    SPECIFIC_NAME = Column(String, nullable=False)
    ROUTINE_CATALOG = Column(String, nullable=False)
    ROUTINE_SCHEMA = Column(String, nullable=False)
    ROUTINE_NAME = Column(String, nullable=False)
    ROUTINE_TYPE = Column(String, nullable=False)
    DATA_TYPE = Column(String, nullable=False)
    CHARACTER_MAXIMUM_LENGTH = Column(Integer)
    CHARACTER_OCTET_LENGTH = Column(Integer)
    NUMERIC_PRECISION = Column(BIGINT)
    NUMERIC_SCALE = Column(Integer)
    DATETIME_PRECISION = Column(BIGINT)
    CHARACTER_SET_NAME = Column(String)
    COLLATION_NAME = Column(String)
    DTD_IDENTIFIER = Column(LONGTEXT)
    ROUTINE_BODY = Column(String, nullable=False)
    ROUTINE_DEFINITION = Column(LONGTEXT)
    EXTERNAL_NAME = Column(String)
    EXTERNAL_LANGUAGE = Column(String)
    PARAMETER_STYLE = Column(String, nullable=False)
    IS_DETERMINISTIC = Column(String, nullable=False)
    SQL_DATA_ACCESS = Column(String, nullable=False)
    SQL_PATH = Column(String)
    SECURITY_TYPE = Column(String, nullable=False)
    CREATED = Column(DateTime, nullable=False)
    LAST_ALTERED = Column(DateTime, nullable=False)
    SQL_MODE = Column(String, nullable=False)
    ROUTINE_COMMENT = Column(LONGTEXT, nullable=False)
    DEFINER = Column(String, nullable=False)
    CHARACTER_SET_CLIENT = Column(String, nullable=False)
    COLLATION_CONNECTION = Column(String, nullable=False)
    DATABASE_COLLATION = Column(String, nullable=False)

