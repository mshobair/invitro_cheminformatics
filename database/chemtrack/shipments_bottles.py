import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class ShipmentBottles(Base):
    """Maps to shipment_bottles table in chemprop databases."""

    __tablename__ = 'shipment_bottles'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    shipment_file_id = Column(Integer)
    plate_barcode = Column(String)
    bottle_id = Column(Integer)
    concentration = Column(Integer)
    concentration_unit = Column(String)
    amount = Column(Integer)
    amount_unit = Column(String)
    barcode = Column(String)
    well_id = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)