import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Engines(Base):
    """Maps to ENGINES table in information databases."""

    __tablename__ = 'ENGINES'
    __table_args__ = {'schema': Schemas.information_schema}
    
    ENGINE = Column(String(64), nullable=False)
    SUPPORT = Column(String(8), nullable=False)
    COMMENT = Column(String(80), nullable=False)
    TRANSACTION = Column(String(3))
    XA = Column(String(3))
    SAVEPOINTS = Column(String(3))
    