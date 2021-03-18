import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class CharacterSets(Base):
    """Maps to CHARACTER_SETS table in information databases."""

    __tablename__ = 'CHARACTER_SETS'
    __table_args__ = {'schema': Schemas.information_schema}

    CHARACTER_SET_NAME = Column(String(32), nullable=False)
    DEFAULT_COLLATE_NAME = Column(String(32), nullable=False)
    DESCRIPTION = Column(String(60), nullable=False)
    MAXLEN = Column(BIGINT, nullable=False, default=0)