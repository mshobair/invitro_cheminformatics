import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbCmpmem(Base):
    """Maps to INNODB_CMPMEM table in information databases."""

    __tablename__ = 'INNODB_CMPMEM'
    __table_args__ = {'schema': Schemas.information_schema}

    page_size = Column(Integer, nullable=False, default=0)
    buffer_pool_instance = Column(Integer, nullable=False, default=0)
    pages_used = Column(Integer, nullable=False, default=0)
    pages_free = Column(Integer, nullable=False, default=0)
    relocation_ops = Column(Integer, nullable=False, default=0)
    relocation_time = Column(Integer, nullable=False, default=0)