import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Bottles(Base):
    """Maps to bottles table in chemprop databases."""

    __tablename__ = 'bottles'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    barcode_parent = Column(String)
    barcode_type = Column(String)
    status = Column(String)
    compound_name = Column(String)
    cas = Column(String)
    cid = Column(String)
    vendor = Column(String)
    vendor_part_number = Column(String)
    qty_available_mg = Column(Integer)
    qty_available_ul = Column(Integer)
    concentration_mm = Column(Integer)
    qty_available_umols = Column(Integer)
    structure_real_amw = Column(String)
    sam = Column(String)
    cpd = Column(String)
    po_number = Column(String)
    lot_number = Column(String)
    form = Column(String)
    date_record_added = Column(String)
    solubility = Column(String)
    solubility_details = Column(String)
    coa_summary_id = Column(Integer)
    can_plate = Column(Integer, default=1)
    barcode = Column(String)
    qty_available_mg_ul = Column(Integer)
    units  = Column(String)
    error = Column(String)
    qc_ts_molwt = Column(String)
    qc_struct_real_amw = Column(String)
    details = Column(String)
    max_plated_conc_mm = Column(String)
    date_modified = Column(String)
    external_bottle = Column(Integer, default=0)
    comment = Column(String)
    freeze_thaw_count = Column(Integer)
    smiles  = Column(String)
    solubility_solvent = Column(String)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)