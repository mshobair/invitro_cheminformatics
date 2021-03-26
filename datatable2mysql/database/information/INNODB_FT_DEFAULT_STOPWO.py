import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbFtDefaultStopwo(Base):
    """Maps to INNODB_FT_DEFAULT_STOPWO table in information databases."""

    __tablename__ = 'INNODB_FT_DEFAULT_STOPWO'
    __table_args__ = {'schema': Schemas.information_schema}

    value = Column(String, nullable=False)