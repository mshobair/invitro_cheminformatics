import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Views(Base):
    """Maps to VIEWS table in information databases."""

    __tablename__ = 'VIEWS'
    __table_args__ = {'schema': Schemas.information_schema}

    TABLE_CATALOG = Column(String, nullable=False)
    TABLE_SCHEMA = Column(String, nullable=False)
    TABLE_NAME = Column(String, nullable=False)
    VIEW_DEFINITION = Column(LONGTEXT, nullable=False)
    CHECK_OPTION = Column(String, nullable=False)
    IS_UPDATABLE = Column(String, nullable=False)
    DEFINER = Column(String, nullable=False)
    SECURITY_TYPE = Column(String, nullable=False)
    CHARACTER_SET_CLIENT = Column(String, nullable=False)
    COLLATION_CONNECTION = Column(String, nullable=False)