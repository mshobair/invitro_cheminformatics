import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbCmpReset(Base):
    """Maps to INNODB_CMP_RESET table in information databases."""

    __tablename__ = 'INNODB_CMP_RESET'
    __table_args__ = {'schema': Schemas.information_schema}

    page_size = Column(Integer, nullable=False, default=0)
    compress_ops = Column(Integer, nullable=False, default=0)
    compress_ops_ok = Column(Integer, nullable=False, default=0)
    compress_time = Column(Integer, nullable=False, default=0)
    uncompress_ops = Column(Integer, nullable=False, default=0)
    uncompress_time = Column(Integer, nullable=False, default=0)