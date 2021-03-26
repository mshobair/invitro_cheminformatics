import datetime

from database.chemprop.threshold_derivations import ThresholdDerivations
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import relationship

from database.base import Base


class Thresholds(Base):
    """Maps to thresholds table in chemprop databases."""

    __tablename__ = "thresholds"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_threshold_derivation_id = Column(ForeignKey(ThresholdDerivations.id))
    min_value = Column(DOUBLE)
    max_value = Column(DOUBLE)
    result_text = Column(String(255))
    result_value = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    threshold_derivation = relationship("ThresholdDerivations")