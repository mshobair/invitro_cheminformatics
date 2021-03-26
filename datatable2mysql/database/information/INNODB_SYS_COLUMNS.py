import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysColumns(Base):
    """Maps to INNODB_SYS_COLUMNS table in information databases."""

    __tablename__ = 'INNODB_SYS_COLUMNS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    NAME = Column(String, nullable=False)
    POS = Column(BIGINT, nullable=False, default=0)
    MTYPE = Column(Integer, nullable=False, default=0)
    PRTYPE = Column(Integer, nullable=False, default=0)
    LEN = Column(Integer, nullable=False, default=0)