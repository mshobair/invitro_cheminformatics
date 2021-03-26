import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class UnivariateCalculations(Base):
    """Maps to univariate_calculations table in qsar databases."""

    __tablename__ = 'univariate_calculations'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_descriptor_id = Column(Integer, nullable=False)
    fk_dataset_id = Column(Integer, nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)