import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class ColumnPrivileges(Base):
    """Maps to COLUMN_PRIVILEGES table in information databases."""

    __tablename__ = 'COLUMN_PRIVILEGES'
    __table_args__ = {'schema': Schemas.information_schema}

    GRANTEE = Column(String(81), nullable=False)
    TABLE_CATALOG = Column(String(512), nullable=False)
    TABLE_SCHEMA = Column(String(64), nullable=False)
    TABLE_NAME = Column(String(64), nullable=False)
    COLUMN_NAME = Column(String(64), nullable=False)
    PRIVILEGE_TYPE = Column(String(64), nullable=False)
    IS_GRANTABLE = Column(String(3), nullable=False)
