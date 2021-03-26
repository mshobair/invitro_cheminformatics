import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Samples(Base):
    """Maps to samples table in chemprop databases."""

    __tablename__ = 'samples'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    source_barcode = Column(String)
    gsid = Column(Integer)
    notes = Column(String)
    data_type = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)