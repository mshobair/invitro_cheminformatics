import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class PlateTypes(Base):
    """Maps to plate_types table in chemprop databases."""

    __tablename__ = 'plate_types'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    label = Column(String)
    numeric_value = Column(Integer)