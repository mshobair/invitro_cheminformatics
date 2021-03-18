import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Contacts(Base):
    """Maps to contacts table in chemprop databases."""

    __tablename__ = 'contacts'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    vendor_id = Column(Integer)
    email = Column(String)
    title = Column(String)
    phone1 = Column(String)
    phone2 = Column(String)
    fax = Column(String)
    cell = Column(String)
    other_details = Column(String)
    department = Column(String)
    contact_type_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)