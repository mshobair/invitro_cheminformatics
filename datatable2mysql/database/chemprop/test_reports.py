import datetime

import pytest
from database.chemprop.qsar_predicted_properties import QsarPredictedProperties
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base

pytestmark = pytest.mark.skip('This is not a test class')

class TestReports(Base):
    """Maps to test_reports table in chemprop databases."""

    __tablename__ = 'test_reports'
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_qsar_predicted_property_id = Column(ForeignKey(QsarPredictedProperties.id))
    html = Column(String(10000))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    qsar_predicted_property = relationship("QsarPredictedProperty")