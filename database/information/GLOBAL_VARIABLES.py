import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class GlobalVariables(Base):
    """Maps to GLOBAL_VARIABLES table in information databases."""

    __tablename__ = 'GLOBAL_VARIABLES'
    __table_args__ = {'schema': Schemas.information_schema}

    VARIABLE_NAME = Column(String, nullable=False)
    VARIABLE_VALUE = Column(String)