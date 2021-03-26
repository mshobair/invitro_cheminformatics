import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class OrderPlateDetails(Base):
    """Maps to order_plate_details table in chemprop databases."""

    __tablename__ = 'order_plate_details'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    order_id = Column(Integer)
    empty = Column(String)
    solvent = Column(String)
    control = Column(String)
    plate_type_id = Column(Integer)
    randomly_placed_controls = Column(Integer, default=0)
    randomly_placed_controls_num = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)