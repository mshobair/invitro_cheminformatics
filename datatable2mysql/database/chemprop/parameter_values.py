import datetime

from database.chemprop.parameter_sets import ParameterSets
from database.chemprop.parameters import Parameters
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class ParameterValues(Base):
    """Maps to parameter_values table in chemprop databases."""

    __tablename__ = "parameter_values"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_parameter_set_id = Column(ForeignKey(ParameterSets.id))
    fk_parameter_id = Column(ForeignKey(Parameters.id))
    value = Column(FLOAT)
    value_text = Column(String(255))
    confidence = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    parameter_set = relationship("ParameterSets")
    parameter = relationship("Parameter")