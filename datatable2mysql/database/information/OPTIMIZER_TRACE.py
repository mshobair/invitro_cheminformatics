import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class OptimizerTrace(Base):
    """Maps to OPTIMIZER_TRACE table in information databases."""

    __tablename__ = 'OPTIMIZER_TRACE'
    __table_args__ = {'schema': Schemas.information_schema}

    QUERY = Column(LONGTEXT, nullable=False)
    TRACE = Column(LONGTEXT, nullable=False)
    MISSING_BYTES_BEYOND_MAX_MEM_SIZE = Column(Integer, nullable=False, default=0)
    INSUFFICIENT_PRIVILEGES = Column(TINYINT, nullable=False, default=0)