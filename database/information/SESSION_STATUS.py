import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class SessionStatus(Base):
    """Maps to SESSION_STATUS table in information databases."""

    __tablename__ = 'SESSION_STATUS'
    __table_args__ = {'schema': Schemas.information_schema}

    VARIABLE_NAME = Column(String, nullable=False)
    VARIABLE_VALUE = Column(String)