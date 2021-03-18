import datetime

from database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from base import Base


class DescriptorSets(Base):
    """Maps to descriptor_sets table in qsar databases."""

    __tablename__ = 'descriptor_sets'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))
    description = Column(String(255))
    software_package = Column(String(255))
    software_version = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
