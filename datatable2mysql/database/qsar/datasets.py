import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Datasets(Base):
    """Maps to datasets table in qsar databases."""

    __tablename__ = 'datasets'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    label = Column(String, nullable=False)
    long_description = Column(String)
    short_description = Column(String)
    version = Column(String)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)