import datetime

from database.database_schemas import Schemas
from database.qsar.models import Models
from database.qsar.statistics import Statistics
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class ModelStatistics(Base):
    """Maps to model_statistics table in qsar databases."""

    __tablename__ = 'model_statistics'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_model_id = Column(ForeignKey(Models.id))
    fk_statistic_id = Column(ForeignKey(Statistics.id))
    set_type = Column(String(255))
    value = Column(FLOAT)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    model = relationship("Models")
    statistic = relationship("Statistics")
