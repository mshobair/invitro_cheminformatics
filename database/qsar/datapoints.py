import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, FLOAT

from database.base import Base


class Datapoints(Base):
    """Maps to datapoints table in qsar databases."""

    __tablename__ = 'datapoints'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_dsstox_compound_id = Column(Integer, nullable=False)
    efk_chemprop_measured_property_id = Column(Integer, nullable=False)
    measured_value_dn = Column(FLOAT)

    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)