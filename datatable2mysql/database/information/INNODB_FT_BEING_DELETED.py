import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbFtBeingDeleted(Base):
    """Maps to INNODB_FT_BEING_DELETED table in information databases."""

    __tablename__ = 'INNODB_FT_BEING_DELETED'
    __table_args__ = {'schema': Schemas.information_schema}

    DOC_ID = Column(BIGINT, nullable=False, default=0)
