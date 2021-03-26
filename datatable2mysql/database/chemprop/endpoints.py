import datetime

from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Endpoints(Base):
    """Maps to endpoints table in chemprop databases."""

    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, nullable=False)
    # fk_endpoint_category_id = Column(ForeignKey(EndpointCategories.id))
    abbreviation = Column(String(255))
    name = Column(String(255))
    description = Column(String(1024))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    standard_unit = Column(String(255))

    # endpoint_category = relationship("EndpointCategories")