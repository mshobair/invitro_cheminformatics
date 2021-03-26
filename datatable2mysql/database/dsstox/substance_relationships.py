import datetime

from database.database_schemas import Schemas
from database.dsstox.generic_substances import GenericSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship

from database.base import Base


class SubstanceRelationships(Base):
    """Maps to substance_relationships table in dsstox databases."""

    __tablename__ = 'substance_relationships'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_generic_substance_id_predecessor = Column(ForeignKey(GenericSubstances.id))
    fk_generic_substance_id_successor = Column(ForeignKey(GenericSubstances.id))
    relationship_ = Column(String(255))
    source = Column(String(255))
    qc_notes = Column(String(1024))
    mixture_percentage = Column(DECIMAL(10, 0))
    percentage_type = Column(String(255))
    is_nearest_structure = Column(Integer)
    is_nearest_casrn = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    generic_substance_predecessor = relationship("GenericSubstances")
    generic_substance_successor = relationship("GenericSubstances")