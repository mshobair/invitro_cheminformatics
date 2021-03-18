import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class TaskOrders(Base):
    """Maps to task_orders table in chemprop databases."""

    __tablename__ = 'task_orders'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    vendor_id = Column(Integer)
    agreement_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    rank = Column(Integer)


    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)