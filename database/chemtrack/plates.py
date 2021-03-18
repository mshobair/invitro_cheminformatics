import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Plates(Base):
    """Maps to plates table in chemprop databases."""

    __tablename__ = 'plates'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    shipment_file_id = Column(Integer)
    plate_count = Column(Integer)
    ship_id = Column(String)
    aliquot_plate_barcode = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)