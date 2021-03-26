import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbFtConfig(Base):
    """Maps to INNODB_FT_CONFIG table in information databases."""

    __tablename__ = 'INNODB_FT_CONFIG'
    __table_args__ = {'schema': Schemas.information_schema}

    KEY = Column(String, nullable=False)
    VALUE = Column(String, nullable=False)