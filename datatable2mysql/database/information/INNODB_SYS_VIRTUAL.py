import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysVirtual(Base):
    """Maps to INNODB_SYS_VIRTUAL table in information databases."""

    __tablename__ = 'INNODB_SYS_VIRTUAL'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_ID = Column(BIGINT, nullable=False, default=0)
    POS = Column(Integer, nullable=False, default=0)
    BASE_POS = Column(Integer, nullable=False, default=0)