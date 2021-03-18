from database.database_schemas import Schemas
from database.dsstox.generic_substances import GenericSubstances
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class SynonymMv(Base):
    """Maps to synonym_mv table in dsstox databases."""

    __tablename__ = 'synonym_mv'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_generic_substance_id = Column(ForeignKey(GenericSubstances.id))
    identifier = Column(String(2000))
    synonym_type = Column(String(50))
    rank = Column(Integer)

    generic_substance = relationship("GenericSubstances")