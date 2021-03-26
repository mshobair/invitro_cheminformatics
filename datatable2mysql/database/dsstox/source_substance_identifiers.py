import datetime

from database.database_schemas import Schemas
from database.dsstox.source_substances import SourceSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class SourceSubstanceIdentifiers(Base):
    """Maps to source_substance_identifiers table in dsstox databases."""

    __tablename__ = 'source_substance_identifiers'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_source_substance_id = Column(ForeignKey(SourceSubstances.id))
    identifier = Column(String(1024))
    identifier_type = Column(String(255))
    fk_source_substance_identifier_parent = Column(ForeignKey('source_substance_identifiers.id'))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    source_substance = relationship("SourceSubstances")
    source_substance_identifier = relationship("SourceSubstanceIdentifiers")
