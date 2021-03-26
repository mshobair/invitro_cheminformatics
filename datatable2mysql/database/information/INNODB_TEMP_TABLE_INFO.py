import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbTempTableInfo(Base):
    """Maps to INNODB_TEMP_TABLE_INFO table in information databases."""

    __tablename__ = 'INNODB_TEMP_TABLE_INFO'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String)
    N_COLS = Column(Integer, nullable=False, default=0)
    SPACE = Column(Integer, nullable=False, default=0)
    PER_TABLE_TABLESPACE = Column(String)
    IS_COMPRESSED = Column(String)