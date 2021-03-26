import datetime

from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class CompoundRelationships(Base):
    """Maps to compound_relationships table in dsstox databases."""

    __tablename__ = 'compound_relationships'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_compound_id_predecessor = Column(ForeignKey(Compounds.id), nullable=False)
    fk_compound_id_successor = Column(ForeignKey(Compounds.id), nullable=False)
    source = Column(String(255))
    relationship_ = Column(String(255)) # underscore at end to differentiate from relationship function
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    compound_predecessor = relationship("Compounds")
    compound_successor = relationship("Compounds")
