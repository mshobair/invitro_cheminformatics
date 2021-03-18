import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Queries(Base):
    """Maps to queries table in chemprop databases."""

    __tablename__ = 'queries'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    label = Column(String)
    description = Column(String)
    sql = Column(String)
    count = Column(Integer)
    conditions = Column(String)
    complete_query = Column(String)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)