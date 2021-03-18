import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysDatafiles(Base):
    """Maps to INNODB_SYS_DATAFILES table in information databases."""

    __tablename__ = 'INNODB_SYS_DATAFILES'
    __table_args__ = {'schema': Schemas.information_schema}

    SPACE = Column(Integer, nullable=False, default=0)
    PATH = Column(String, nullable=False)