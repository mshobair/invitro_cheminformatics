import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class AssayReference(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_reference'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    reference_id = Column(Integer, nullable=False, primary_key=True)
    aid = Column(Integer, nullable=False)
    citation_id = Column(Integer, nullable=False)
