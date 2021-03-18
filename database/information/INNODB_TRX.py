import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT

from database.base import Base


class InnodbTrx(Base):
    """Maps to INNODB_TRX table in information databases."""

    __tablename__ = 'INNODB_TRX'
    __table_args__ = {'schema': Schemas.information_schema}

    trx_id = Column(String, nullable=False)
    trx_state = Column(String, nullable=False)
    trx_started = Column(DateTime, nullable=False)
    trx_requested_lock_id = Column(String)
    trx_wait_started = Column(DateTime)
    trx_weight = Column(BIGINT, nullable=False, default=0)
    trx_mysql_thread_id = Column(BIGINT, nullable=False, default=0)
    trx_query = Column(String)
    trx_operation_state = Column(String)
    trx_tables_in_use = Column(BIGINT, nullable=False, default=0)
    trx_tables_locked = Column(BIGINT, nullable=False, default=0)
    trx_lock_structs = Column(BIGINT, nullable=False, default=0)
    trx_lock_memory_bytes = Column(BIGINT, nullable=False, default=0)
    trx_rows_locked = Column(BIGINT, nullable=False, default=0)
    trx_rows_modified = Column(BIGINT, nullable=False, default=0)
    trx_concurrency_tickets = Column(BIGINT, nullable=False, default=0)
    trx_isolation_level = Column(String, nullable=False)
    trx_unique_checks = Column(Integer, nullable=False, default=0)
    trx_foreign_key_checks = Column(Integer, nullable=False, default=0)
    trx_last_foreign_key_error = Column(String)
    trx_adaptive_hash_latched = Column(Integer, nullable=False, default=0)
    trx_adaptive_hash_timeout = Column(BIGINT, nullable=False, default=0)
    trx_is_read_only = Column(Integer, nullable=False, default=0)
    trx_autocommit_non_locking = Column(Integer, nullable=False, default=0)