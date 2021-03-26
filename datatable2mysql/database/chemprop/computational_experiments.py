import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class ComputationalExperiments(Base):
    """Maps to computational_experiments table in chemprop databases."""

    __tablename__ = 'computational_experiments'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    efk_qsar_model_id = Column(Integer)
    efk_generic_substance_id_dn = Column(Integer)
    fk_input_set_id = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)