import datetime

from database.chemprop.endpoints import Endpoints
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class ThresholdDerivations(Base):
    """Maps to threshold_derivations table in chemprop databases."""

    __tablename__ = "threshold_derivations"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_endpoint_id_unthresholded = Column(ForeignKey(Endpoints.id))
    fk_endpoint_id_thresholded = Column(ForeignKey(Endpoints.id))
    name = Column(String(255))
    label = Column(String(255))
    short_description = Column(String(255))
    long_description = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    endpoint_unthresholded = relationship("Endpoints")
    endpoint_thresholded = relationship("Endpoints")