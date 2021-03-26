import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class ReferentialConstraints(Base):
    """Maps to REFERENTIAL_CONSTRAINTS table in information databases."""

    __tablename__ = 'REFERENTIAL_CONSTRAINTS'
    __table_args__ = {'schema': Schemas.information_schema}

    CONSTRAINT_CATALOG = Column(String, nullable=False)
    CONSTRAINT_SCHEMA = Column(String, nullable=False)
    CONSTRAINT_NAME = Column(String, nullable=False)
    UNIQUE_CONSTRAINT_CATALOG = Column(String, nullable=False)
    UNIQUE_CONSTRAINT_SCHEMA = Column(String, nullable=False)
    UNIQUE_CONSTRAINT_NAME = Column(String)
    MATCH_OPTION = Column(String, nullable=False)
    UPDATE_RULE = Column(String, nullable=False)
    DELETE_RULE = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False)
    REFERENCED_TABLE_NAME = Column(String, nullable=False)