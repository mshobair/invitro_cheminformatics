import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class GlobalStatus(Base):
    """Maps to GLOBAL_STATUS table in information databases."""

    __tablename__ = 'GLOBAL_STATUS'
    __table_args__ = {'schema': Schemas.information_schema}

    VARIABLE_NAME = Column(String(64), nullable=False)
    VARIABLE_VALUE = Column(String)