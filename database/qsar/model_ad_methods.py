import datetime

from database.database_schemas import Schemas
from database.qsar.ad_methods import AdMethods
from database.qsar.models import Models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class ModelAdMethods(Base):
    """Maps to model_ad_methods table in qsar databases."""

    __tablename__ = 'model_ad_methods'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_ad_method_id = Column(ForeignKey(AdMethods.id))
    fk_model_id = Column(ForeignKey(Models.id))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    ad_method = relationship("AdMethods")
    model = relationship("Models")
