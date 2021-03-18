import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class CollationCharacterSets(Base):
    """Maps to COLLATION_CHARACTER_SETS table in information databases."""

    __tablename__ = 'COLLATION_CHARACTER_SETS'
    __table_args__ = {'schema': Schemas.information_schema}

    COLLATION_NAME = Column(String(32), nullable=False)
    CHARACTER_SET_NAME = Column(String(32), nullable=False)