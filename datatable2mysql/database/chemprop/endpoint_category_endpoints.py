import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class EndpointCategoryEndpoints(Base):
    """Maps to endpoint_category_endpoints table in chemprop databases."""

    __tablename__ = 'endpoint_category_endpoints'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_endpoint_category_id = Column(Integer)
    fk_endpoint_id = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)