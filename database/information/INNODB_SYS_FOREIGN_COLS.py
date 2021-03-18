import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysForeignCols(Base):
    """Maps to INNODB_SYS_FOREIGN_COLS table in information databases."""

    __tablename__ = 'INNODB_SYS_FOREIGN_COLS'
    __table_args__ = {'schema': Schemas.information_schema}

    ID = Column(String, nullable=False)
    FOR_COL_NAME = Column(String, nullable=False)
    REF_COL_NAME = Column(String, nullable=False)
    POS = Column(Integer, nullable=False, default=0)