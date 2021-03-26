import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class OrderConcentrations(Base):
    """Maps to order_concentrations table in chemprop databases."""

    __tablename__ = 'order_concentrations'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    concentration = Column(Integer)
    unit = Column(String)