import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class UsersTaskOrders(Base):
    """Maps to users_task_orders table in chemprop databases."""

    __tablename__ = 'users_task_orders'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    task_order_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)