import datetime

from database.database_schemas import Schemas
from database.dsstox.generic_substances import GenericSubstances
from database.dsstox.source_substances import SourceSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from database.base import Base


class SourceGenericSubstanceMappings(Base):
    """Maps to source_generic_substance_mappings table in dsstox databases."""

    __tablename__ = 'source_generic_substance_mappings'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_source_substance_id = Column(ForeignKey(SourceSubstances.id))
    fk_generic_substance_id = Column(ForeignKey(GenericSubstances.id))
    connection_reason = Column(String(255))
    linkage_score = Column(FLOAT)
    curator_validated = Column(Integer)
    qc_notes = Column(String(1024))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    source_substance = relationship("SourceSubstances")
    generic_substance = relationship("GenericSubstances")
