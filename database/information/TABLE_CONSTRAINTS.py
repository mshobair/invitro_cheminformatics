import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class TableConstraints(Base):
    """Maps to TABLE_CONSTRAINTS table in information databases."""

    __tablename__ = 'TABLE_CONSTRAINTS'
    __table_args__ = {'schema': Schemas.information_schema}

    CONSTRAINT_CATALOG = Column(String, nullable=False)
    CONSTRAINT_SCHEMA = Column(String, nullable=False)
    CONSTRAINT_NAME = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False)
    CONSTRAINT_NAME = Column(String, nullable=False)