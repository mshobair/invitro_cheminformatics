import datetime

from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.qsar.models import Models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class QsarPredictedProperties(Base):
    """Maps to qsar_predicted_properties table in chemprop databases."""

    __tablename__ = 'qsar_predicted_properties'
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_dsstox_compound_id = Column(ForeignKey(Compounds.id))
    efk_qsar_model_id = Column(ForeignKey(Models.id))
    result_value = Column(FLOAT)
    result_min = Column(FLOAT)
    result_max = Column(FLOAT)
    result_error = Column(FLOAT)
    result_text = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    compound = relationship("Compounds")
    model = relationship("Models")