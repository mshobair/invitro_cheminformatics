import datetime

from database.database_schemas import Schemas
from database.dsstox.generic_substances import GenericSubstances
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class OtherCasrns(Base):
    """Maps to other_casrns table in dsstox databases."""

    __tablename__ = 'other_casrns'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_generic_substance_id = Column(ForeignKey(GenericSubstances.id))
    casrn = Column(String(255), nullable=False)
    cas_type = Column(String(255), nullable=False)
    source = Column(String(255), nullable=False)
    qc_notes = Column(String(1024))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    generic_substance = relationship("GenericSubstances")
