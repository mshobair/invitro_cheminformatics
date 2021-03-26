import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class DatasetDatapoints(Base):
    """Maps to dataset_datapoints table in qsar databases."""

    __tablename__ = 'dataset_datapoints'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_dataset_id = Column(Integer, nullable=False)
    fk_datapoint_id = Column(Integer, nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)