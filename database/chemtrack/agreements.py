import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Agreements(Base):
    """Maps to agreements table in chemprop databases."""

    __tablename__ = 'agreements'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    agreement_status_id = Column(Integer)
    vendor_id = Column(Integer)
    description = Column(String)
    expiration_date_depr = Column(String)
    created_by = Column(String)
    active = Column(Integer, default=0)
    revoke_reason = Column(String)
    user_id = Column(Integer)
    rank = Column(Integer)
    expiration_date = Column(DateTime)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)