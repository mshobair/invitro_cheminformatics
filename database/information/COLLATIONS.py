import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class Collations(Base):
    """Maps to COLLATIONS table in information databases."""

    __tablename__ = 'COLLATIONS'
    __table_args__ = {'schema': Schemas.information_schema}

    COLLATION_NAME = Column(String(32), nullable=False)
    CHARACTER_SET_NAME = Column(String(32), nullable=False)
    ID = Column(BIGINT,nullable=False, default=0)
    IS_DEFAULT = Column(String(3), nullable=False)
    IS_COMPILED = Column(String(3), nullable=False)
    SORTLEN = Column(BIGINT, nullable=False, default=0)