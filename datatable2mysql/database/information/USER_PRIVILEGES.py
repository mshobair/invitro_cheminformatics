import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class UserPrivileges(Base):
    """Maps to USER_PRIVILEGES table in information databases."""

    __tablename__ = 'USER_PRIVILEGES'
    __table_args__ = {'schema': Schemas.information_schema}

    GRANTEE = Column(String, nullable=False)
    TABLE_CATALOG = Column(String, nullable=False)
    PRIVILEGE_TYPE = Column(String, nullable=False)
    IS_GRANTABLE = Column(String, nullable=False)