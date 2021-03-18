import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbSysForeign(Base):
    """Maps to INNODB_SYS_FOREIGN table in information databases."""

    __tablename__ = 'INNODB_SYS_FOREIGN'
    __table_args__ = {'schema': Schemas.information_schema}

    ID = Column(String, nullable=False)
    FOR_NAME = Column(String, nullable=False)
    REF_NAME = Column(String, nullable=False)
    N_COLS = Column(Integer, nullable=False, default=0)
    TYPE = Column(Integer, nullable=False, default=0)