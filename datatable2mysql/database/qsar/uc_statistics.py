import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, FLOAT

from database.base import Base


class UcStatistics(Base):
    """Maps to uc_statistics table in qsar databases."""

    __tablename__ = 'uc_statistics'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(FLOAT)
    fk_univ_calc_id = Column(Integer, nullable=False)
    fk_statistic_id = Column(Integer, nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)