import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbFtIndexTable(Base):
    """Maps to INNODB_FT_INDEX_TABLE table in information databases."""

    __tablename__ = 'INNODB_FT_INDEX_TABLE'
    __table_args__ = {'schema': Schemas.information_schema}

    WORD = Column(String, nullable=False)
    FIRST_DOC_ID = Column(BIGINT, nullable=False, default=0)
    LAST_DOC_ID = Column(BIGINT, nullable=False, default=0)
    DOC_COUNT = Column(BIGINT, nullable=False, default=0)
    DOC_ID = Column(BIGINT, nullable=False, default=0)
    POSITION = Column(BIGINT, nullable=False, default=0)