import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysTablespaces(Base):
    """Maps to INNODB_SYS_TABLESPACES table in information databases."""

    __tablename__ = 'INNODB_SYS_TABLESPACES'
    __table_args__ = {'schema': Schemas.information_schema}

    SPACE = Column(Integer, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    FLAG = Column(Integer, nullable=False, default=0)
    FILE_FORMAT = Column(String)
    ROW_FORMAT = Column(String)
    PAGE_SIZE = Column(String, nullable=False)
    ZIP_PAGE_SIZE = Column(Integer, nullable=False, default=0)
    SPACE_TYPE = Column(String)
    FS_BLOCK_SIZE = Column(Integer, nullable=False, default=0)
    FILE_SIZE = Column(BIGINT, nullable=False, default=0)
    ALLOCATED_SIZE = Column(BIGINT, nullable=False, default=0)