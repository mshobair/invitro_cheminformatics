import datetime

from database.base import Base
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.dsstox.chemical_lists import ChemicalLists


class SourceSubstances(Base):
    """Maps to source_substances table in dsstox databases."""

    __tablename__ = 'source_substances'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_chemical_list_id = Column(ForeignKey(ChemicalLists.id))
    dsstox_record_id = Column(String(255))
    external_id = Column(String(255))
    warnings = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    qc_notes = Column(String(255))

    chemical_list = relationship("ChemicalLists")
