import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class AssayComponentMap(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_component_map'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    acid = Column(Integer, nullable=False, primary_key=True)
    acsn = Column(String(255), nullable=False, primary_key=True)
