import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Parameters(Base):
    """Maps to PARAMETERS table in information databases."""

    __tablename__ = 'PARAMETERS'
    __table_args__ = {'schema': Schemas.information_schema}

    SPECIFIC_CATALOG = Column(String, nullable=False)
    SPECIFIC_SCHEMA = Column(String, nullable=False)
    SPECIFIC_NAME = Column(String, nullable=False)
    ORDINAL_POSITION = Column(Integer, nullable=False, default=0)
    PARAMETER_MODE = Column(String)
    PARAMETER_NAME = Column(String)
    DATA_TYPE = Column(String, nullable=False)
    CHARACTER_MAXIMUM_LENGTH = Column(Integer)
    CHARACTER_OCTET_LENGTH = Column(Integer)
    NUMERIC_PRECISION = Column(BIGINT)
    NUMERIC_SCALE = Column(Integer)
    DATETIME_PRECISION = Column(BIGINT)
    CHARACTER_SET_NAME = Column(String)
    COLLATION_NAME = Column(String)
    DTD_IDENTIFIER = Column(LONGTEXT, nullable=False)
    ROUTINE_TYPE = Column(String, nullable=False)