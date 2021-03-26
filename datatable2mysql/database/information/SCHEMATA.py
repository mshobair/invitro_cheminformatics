import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Schemata(Base):
    """Maps to SCHEMATA table in information databases."""

    __tablename__ = 'SCHEMATA'
    __table_args__ = {'schema': Schemas.information_schema}

    CATALOG_NAME = Column(String, nullable=False)
    SCHEMA_NAME = Column(String, nullable=False)
    DEFAULT_CHARACTER_SET_NAME = Column(String, nullable=False)
    DEFAULT_COLLATION_NAME = Column(String, nullable=False)
    SQL_PATH = Column(String, nullable=False)