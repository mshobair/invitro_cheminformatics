import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Tablespaces(Base):
    """Maps to TABLESPACES table in information databases."""

    __tablename__ = 'TABLESPACES'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLESPACE_NAME = Column(String, nullable=False)
    ENGINE = Column(String, nullable=False)
    TABLESPACE_TYPE = Column(String)
    LOGFILE_GROUP_NAME = Column(String)
    EXTENT_SIZE = Column(BIGINT)
    AUTOEXTEND_SIZE = Column(BIGINT)
    MAXIMUM_SIZE = Column(BIGINT)
    NODEGROUP_ID = Column(BIGINT)
    TABLESPACE_COMMENT = Column(String)