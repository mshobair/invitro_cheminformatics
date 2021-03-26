import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class PredictedProperties(Base):
    """Maps to predicted_properties table in chemprop databases."""

    __tablename__ = 'predicted_properties'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_computational_experiment_id = Column(Integer)
    result_value = Column(float)
    result_min = Column(float)
    result_max = Column(float)
    result_error = Column(float)
    result_text = Column(String)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)