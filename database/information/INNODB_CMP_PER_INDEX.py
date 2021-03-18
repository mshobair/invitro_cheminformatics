import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbCmpPerIndex(Base):
    """Maps to INNODB_CMP_PER_INDEX table in information databases."""

    __tablename__ = 'INNODB_CMP_PER_INDEX'
    __table_args__ = {'schema': Schemas.information_schema}

    database_name = Column(String, nullable=False)
    table_name = Column(String, nullable=False)
    index_name = Column(String, nullable=False)
    compress_ops = Column(Integer, nullable=False, default=0)
    compress_ops_ok = Column(Integer, nullable=False, default=0)
    compress_time = Column(Integer, nullable=False, default=0)
    uncompress_ops = Column(Integer, nullable=False, default=0)
    uncompress_time = Column(Integer, nullable=False, default=0)