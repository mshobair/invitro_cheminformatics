import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class CoaSummaries(Base):
    """Maps to coa_summaries table in chemprop databases."""

    __tablename__ = 'coa_summaries'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    bottle_barcode = Column(String)
    coa_table_entry = Column(Integer)
    coa = Column(String)
    msds = Column(String)
    inventory_source = Column(String)
    coa_product_no = Column(String)
    coa_lot_number = Column(String)
    coa_chemical_name = Column(String)
    coa_casrn = Column(String)
    coa_molecular_weight = Column(Integer)
    coa_density = Column(String)
    coa_purity_percentage = Column(String)
    coa_methods = Column(String)
    coa_test_date = Column(String)
    coa_expiration_date = Column(String)
    msds_cautions = Column(String)
    coa_review_notes = Column(String)
    reviewer_initials = Column(String)
    commercial_source = Column(String)
    user_id = Column(Integer)
    gsid = Column(Integer)
    date_record_added = Column(String)
    date_record_modified = Column(String)
    source_substance_id = Column(Integer)
    chemical_list_id = Column(Integer)



    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)