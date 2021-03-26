import datetime

from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.qsar.descriptors import Descriptors
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT

from database.base import Base


class CompoundDescriptors(Base):
    """Maps to compound_desciptors table in qsar databases."""

    __tablename__ = 'compound_descriptors'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=True)
    fk_descriptor_set_id = Column(ForeignKey(Descriptors.id))
    index_number = Column(Integer, nullable=True)
    descriptors_name = Column(String(255), nullable=True)
    short_description = Column(String(255), nullable=True)
    long_description = Column(String(255), nullable=True)
    label = Column(String(255), nullable=True)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    descriptor_image = Column(String(255), nullable=True)

