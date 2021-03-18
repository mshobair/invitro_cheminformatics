import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class AssaySource(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_source'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    asid = Column(Integer, nullable=False, primary_key=True)
    assay_source_name = Column(String(255), nullable=False)
    assay_source_long_name = Column(String(255))
    assay_source_desc = Column(String(255))