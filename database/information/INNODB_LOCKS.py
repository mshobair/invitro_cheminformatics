import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbLocks(Base):
    """Maps to INNODB_LOCKS table in information databases."""

    __tablename__ = 'INNODB_LOCKS'
    __table_args__ = {'schema': Schemas.information_schema}

    lock_id = Column(String, nullable=False)
    lock_trx_id = Column(String, nullable=False)
    lock_mode = Column(String, nullable=False)
    lock_type = Column(String, nullable=False)
    lock_table = Column(String, nullable=False)
    lock_index = Column(String)
    lock_space = Column(BIGINT)
    lock_page = Column(BIGINT)
    lock_rec = Column(BIGINT)
    lock_data = Column(String)