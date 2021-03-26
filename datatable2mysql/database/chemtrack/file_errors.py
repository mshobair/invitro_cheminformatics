import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class FileErrors(Base):
    """Maps to file_errors table in chemprop databases."""

    __tablename__ = 'file_errors'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    error_a = Column(String)
    error_b = Column(String)
    error_count = Column(Integer)
    errorable_id = Column(Integer)
    errorable_type = Column(String)
    error_c = Column(String)


    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)