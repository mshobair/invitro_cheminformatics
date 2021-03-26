import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class InputSetMeasuredProperties(Base):
    """Maps to input_set_measured_properties table in chemprop databases."""

    __tablename__ = 'input_set_measured_properties'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_measured_property_id = Column(Integer)
    fk_input_set_id = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)