import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class ChemicalLists(Base):
    """Maps to chemical_lists table in dsstox databases."""

    __tablename__ = 'chemical_lists'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    list_abbreviation = Column(String(50), nullable=False)
    list_name = Column(String(255), nullable=False)
    list_description = Column(String)
    ncct_contact = Column(String(255), nullable=False)
    source_contact = Column(String(255), nullable=False)
    source_contact_email = Column(String(255), nullable=False)
    source_website = Column(String(1024))
    source_chemical_url_prefix = Column(String(1024))
    source_reference = Column(String(1024))
    source_doi = Column(String(255))
    input_weighting = Column(String(255))
    list_type = Column(String(255), nullable=False)
    list_update_mechanism = Column(String(255), nullable=False)
    list_accessibility = Column(String(255), nullable=False)
    curation_complete = Column(Integer, nullable=False)
    source_data_updated_at = Column(DateTime, nullable=False)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
