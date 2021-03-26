import datetime

from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.dsstox.generic_substances import GenericSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class GenericSubstanceCompounds(Base):
    """Maps to generic_substance_compounds table in dsstox databases."""

    __tablename__ = 'generic_substance_compounds'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_generic_substance_id = Column(ForeignKey(GenericSubstances.id))
    fk_compound_id = Column(ForeignKey(Compounds.id))
    relationship_ = Column(String(255))
    source = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    generic_substance = relationship("GenericSubstances")
    compounds = relationship("Compounds")
