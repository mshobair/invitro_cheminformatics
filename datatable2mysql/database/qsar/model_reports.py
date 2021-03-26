import datetime

from database.database_schemas import Schemas
from database.qsar.models import Models
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import BLOB
from sqlalchemy.orm import relationship

from database.base import Base


class ModelReports(Base):
    """Maps to model_reports table in qsar databases."""

    __tablename__ = 'model_reports'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_model_id = Column(ForeignKey(Models.id))
    report_pdf = Column(BLOB)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    model = relationship("Models")
