import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class ChemicalLibrary(Base):
    """Maps to chemical_library table in invitrodb databases."""

    __tablename__ = 'chemical_library'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    chid = Column(Integer, nullable=False, primary_key=True)
    clib = Column(String(30), nullable=False, primary_key=True)