import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class CoaSummaryFiles(Base):
    """Maps to coa_summary_files table in chemprop databases."""

    __tablename__ = 'coa_summary_files'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    filename = Column(String)
    file_url = Column(String)
    file_kilobytes = Column(Integer)
    coa_summary_count = Column(Integer)
    is_valid = Column(Integer)
    description = Column(String)
    record_error = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)