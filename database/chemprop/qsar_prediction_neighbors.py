import datetime

from database.chemprop.measured_properties import MeasuredProperties
from database.chemprop.qsar_predicted_properties import QsarPredictedProperties
from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class QsarPredictionNeighbors(Base):
    """Maps to qsar_prediction_neighbors table in chemprop databases."""

    __tablename__ = 'qsar_prediction_neighbors'
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_qsar_predicted_property_id = Column(ForeignKey(QsarPredictedProperties.id))
    fk_measured_property_id = Column(ForeignKey(MeasuredProperties.id))
    efk_dsstox_compound_id = Column(ForeignKey(Compounds.id))
    neighbor_number = Column(FLOAT)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    qsar_predicted_property = relationship("QsarPredictedProperties")
    measured_property = relationship("MeasuredProperties")
    compound = relationship("Compounds")