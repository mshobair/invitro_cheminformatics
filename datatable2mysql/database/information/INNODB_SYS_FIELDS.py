import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysFields(Base):
    """Maps to INNODB_SYS_FIELDS table in information databases."""

    __tablename__ = 'INNODB_SYS_FIELDS'
    __table_args__ = {'schema': Schemas.information_schema}

    INDEX_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    POS = Column(Integer, nullable=False, default=0)