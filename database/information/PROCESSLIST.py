import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Processlist(Base):
    """Maps to PROCESSLIST table in information databases."""

    __tablename__ = 'PROCESSLIST'
    __table_args__ = {'schema': Schemas.information_schema}

    ID = Column(BIGINT, nullable=False, default=0)
    USER = Column(String, nullable=False)
    HOST = Column(String, nullable=False)
    DB = Column(String)
    COMMAND = Column(String, nullable=False)
    TIME = Column(Integer, nullable=False, default=0)
    STATE = Column(String)
    INFO = Column(LONGTEXT)