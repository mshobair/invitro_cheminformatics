import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class ShipmentActivities(Base):
    """Maps to shipment_activities table in chemprop databases."""

    __tablename__ = 'shipment_activities'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    action = Column(String)
    location_a = Column(String)
    location_b = Column(String)
    trackable_id = Column(Integer)
    trackable_type = Column(String)
    order_number = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)