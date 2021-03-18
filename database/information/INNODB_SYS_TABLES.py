import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysTables(Base):
    """Maps to INNODB_SYS_TABLES table in information databases."""

    __tablename__ = 'INNODB_SYS_TABLES'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    FLAG = Column(Integer, nullable=False, default=0)
    N_COLS = Column(Integer, nullable=False, default=0)
    SPACE = Column(Integer, nullable=False, default=0)
    FILE_FORMAT = Column(String)
    ROW_FORMAT = Column(String)
    ZIP_PAGE_SIZE = Column(Integer, nullable=False, default=0)
    SPACE_TYPE = Column(String)