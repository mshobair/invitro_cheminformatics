import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class AgreementDocuments(Base):
    """Maps to agreement_documents table in chemprop databases."""

    __tablename__ = 'agreement_documents'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    agreement_id = Column(Integer)
    file_size = Column(Integer)
    file_name = Column(String)
    file_url = Column(String)
    filename = Column(String)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)