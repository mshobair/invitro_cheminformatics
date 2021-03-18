import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class DelayedJobs(Base):
    """Maps to delayed_jobs table in chemprop databases."""

    __tablename__ = 'delayed_jobs'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    priority = Column(Integer, default=0, nullable=False)
    attempts = Column(Integer, default=0, nullable=False)
    handler = Column(String, nullable=False)
    last_error = Column(String)
    run_at = Column(DateTime)
    locked_at = Column(DateTime)
    failed_at = Column(DateTime)
    locked_by = Column(String)
    queue = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    progress_stage = Column(String)
    progress_current = Column(Integer)
    progress_max = Column(Integer)
    comit_id = Column(Integer)
    job_id = Column(Integer)
    job_type = Column(String)