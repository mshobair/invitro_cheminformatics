import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class EndpointCategories(Base):
    """Maps to endpoint_categories table in chemprop databases."""

    __tablename__ = "endpoint_categories"

    id = Column(Integer, primary_key=True, nullable=False)
    fk_endpoint_category_id_parent = Column(Integer, ForeignKey('endpoint_categories.id'))
    abbreviation = Column(String(255))
    name = Column(String(255))
    description = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    endpoint_category_parent = relationship("EndpointCategories", remote_side=[id])