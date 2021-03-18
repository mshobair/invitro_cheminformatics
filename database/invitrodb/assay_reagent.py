import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class AssayReagent(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_reagent'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    arid = Column(Integer, nullable=False, primary_key=True)
    aid = Column(Integer, nullable=False)
    reagent_name_value = Column(String(255))
    reagent_name_value_type = Column(String(255))
    culture_or_assay = Column(String(255))
