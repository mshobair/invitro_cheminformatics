import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.base import Base


class CompoundDescriptorSets(Base):
    """Maps to compound_descriptor_sets table in qsar databases."""

    __tablename__ = 'compound_descriptor_sets'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_dsstox_compound_id = Column(Integer, nullable=False)
    fk_descriptor_set_id = Column(Integer, nullable=False)
    descriptor_string_tsv = Column(String, nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
