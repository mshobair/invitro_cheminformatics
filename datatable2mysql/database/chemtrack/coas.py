import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Coas(Base):
    """Maps to coas table in chemprop databases."""

    __tablename__ = 'coas'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String)
    file_url = Column(String)
    file_kilobytes = Column(Integer)
    user_id = Column(Integer)
    coa_summary_id = Column(Integer)
    barcode = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)