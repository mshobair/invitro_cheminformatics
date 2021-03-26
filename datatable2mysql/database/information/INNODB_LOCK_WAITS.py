import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbLockWaits(Base):
    """Maps to INNODB_LOCK_WAITS table in information databases."""

    __tablename__ = 'INNODB_LOCK_WAITS'
    __table_args__ = {'schema': Schemas.information_schema}

    requesting_trx_id = Column(String, nullable=False)
    requested_lock_id = Column(String, nullable=False)
    blocking_trx_id = Column(String, nullable=False)
    blocking_lock_id = Column(String, nullable=False)