import datetime

from database.database_schemas import Schemas
from database.dsstox.qc_levels import QcLevels
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.base import Base


class GenericSubstances(Base):
    """Maps to generic_substance table in dsstox databases."""

    __tablename__ = 'generic_substances'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_qc_level_id = Column(ForeignKey(QcLevels.id))
    dsstox_substance_id = Column(String(255))
    casrn = Column(String(255))
    preferred_name = Column(String(255))
    substance_type = Column(String(255))
    qc_notes = Column(String(1024))
    qc_notes_private = Column(String(1024))
    source = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    qc_level = relationship("QcLevels")
