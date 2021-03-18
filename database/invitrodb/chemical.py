import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class Chemical(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'Chemical'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    chid = Column(Integer, nullable=False, primary_key=True, default=0)
    casrn = Column(String(45), nullable=False)
    chnm = Column(String(255), nullable=False)