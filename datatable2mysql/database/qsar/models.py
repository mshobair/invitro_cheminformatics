import datetime

from database.chemprop.endpoints import Endpoints
from database.chemprop.parameter_sets import ParameterSets
from database.database_schemas import Schemas
from database.qsar.descriptor_sets import DescriptorSets
from database.qsar.learning_methods import LearningMethods
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Models(Base):
    """Maps to models table in qsar databases."""

    __tablename__ = 'models'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_descriptor_set_id = Column(ForeignKey(DescriptorSets.id))
    fk_learning_method_id = Column(ForeignKey(LearningMethods.id))
    efk_chemprop_endpoint_id = Column(ForeignKey(Endpoints.id))
    name = Column(String(255))
    description = Column(String(255))
    category = Column(String(255))
    source = Column(String(255))
    reference = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    efk_chemprop_parameter_set_id = Column(ForeignKey(ParameterSets.id))
    number_of_descriptors = Column(Integer)
    data_accessibility = Column(String(255), nullable=False)

    descriptor_set = relationship("DescriptorSets")
    learning_method = relationship("LearningMethods")
    endpoint = relationship("Endpoints")
    parameter_set = relationship("ParameterSets")
