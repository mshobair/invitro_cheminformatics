import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Vendors(Base):
    """Maps to vendors table in chemprop databases."""

    __tablename__ = 'vendors'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    label = Column(String)
    phone1 = Column(String)
    phone2 = Column(String)
    other_details = Column(String)
    short_name = Column(String)
    contact_name = Column(String)
    contact_title = Column(String)
    epa_contact_name = Column(String)
    fax = Column(String)
    email = Column(String)
    date = Column(String)
    category = Column(String)
    mta_partner =Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)