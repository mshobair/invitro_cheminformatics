import datetime

from database.database_schemas import Schemas
from database.qsar.descriptor_sets import DescriptorSets
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Descriptors(Base):
    """Maps to descriptors table in qsar databases."""

    __tablename__ = 'descriptors'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_descriptor_set_id = Column(ForeignKey(DescriptorSets.id))
    index_number = Column(Integer)
    descriptors_name = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    long_description = Column(String(1024))
    short_description = Column(String(255))
    label = Column(String(255))

    descriptor_set = relationship("DescriptorSets")