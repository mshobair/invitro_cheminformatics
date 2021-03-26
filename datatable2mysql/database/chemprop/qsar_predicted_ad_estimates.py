import datetime

from database.chemprop.qsar_predicted_properties import QsarPredictedProperties
from database.database_schemas import Schemas
from database.qsar.ad_methods import AdMethods
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class QsarPredictedAdEstimates(Base):
    """Maps to qsar_predicted_ad_estimates table in chemprop databases."""

    __tablename__ = 'qsar_predicted_ad_estimates'
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_qsar_ad_method_id = Column(ForeignKey(AdMethods.id))
    fk_qsar_predicted_property_id = Column(ForeignKey(QsarPredictedProperties.id))
    applicability_value = Column(FLOAT)
    applicability_flag = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    ad_method = relationship("AdMethods")
    qsar_predicted_property = relationship("QsarPredictedProperties")
