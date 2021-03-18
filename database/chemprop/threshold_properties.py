import datetime

from database.chemprop.measured_properties import MeasuredProperties
from database.chemprop.qsar_predicted_properties import QsarPredictedProperties
from database.chemprop.thresholds import Thresholds
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class ThresholdProperties(Base):
    """Maps to threshold_properties table in chemprop databases."""

    __tablename__ = "threshold_properties"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_qsar_predicted_property_id = Column(ForeignKey(QsarPredictedProperties.id))
    fk_measured_property_id = Column(ForeignKey(MeasuredProperties.id))
    fk_threshold_id = Column(ForeignKey(Thresholds.id))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    qsar_predicted_property = relationship("QsarPredictedProperties")
    measured_property = relationship("MeasuredProperties")
    threshold = relationship("Thresholds")
