import datetime

from database.chemprop.endpoints import Endpoints
from database.chemprop.measurement_methods import MeasurementMethods
from database.chemprop.parameter_sets import ParameterSets
from database.database_schemas import Schemas
from database.dsstox.source_substances import SourceSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class MeasuredProperties(Base):
    """Maps to measured_properties table in chemprop databases."""

    __tablename__ = "measured_properties"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_dsstox_source_substance_id = Column(ForeignKey(SourceSubstances.id))
    fk_endpoint_id = Column(ForeignKey(Endpoints.id))
    fk_parameter_set_id = Column(ForeignKey(ParameterSets.id))
    fk_measurement_method_id = Column(ForeignKey(MeasurementMethods.id))
    result_value = Column(FLOAT)
    result_min = Column(FLOAT)
    result_max = Column(FLOAT)
    result_error = Column(FLOAT)
    result_text = Column(String(255))
    result_concerns = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    dsstox_source_substance = relationship("SourceSubstances")
    endpoint = relationship("Endpoints")
    parameter_set = relationship("ParameterSets")
    measurement_method = relationship("MeasurementMethods")