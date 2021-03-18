import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Orders(Base):
    """Maps to orers table in chemprop databases."""

    __tablename__ = 'orers'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    vendor_id = Column(Integer)
    task_order_id = Column(Integer)
    amount = Column(Integer)
    order_status_id  = Column(Integer)
    chemical_list_id = Column(Integer)
    address_id = Column(Integer)
    order_concentration_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    rejected = Column(Integer, default=0)
    resubmitted = Column(Integer, default=0)
    dried_down = Column(Integer, default=0)
    using_standard_replicates = Column(Integer, default=0)
