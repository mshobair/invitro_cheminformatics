import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, FLOAT

from database.base import Base


class VialDetails(Base):
    """Maps to vial_details table in chemprop databases."""

    __tablename__ = 'vial_details'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    ism = Column(String)
    sample_id = Column(String)
    structure_id = Column(String)
    structure_real_amw = Column(DECIMAL)
    sample_supplier = Column(String)
    supplier_structure_id = Column(String)
    aliquot_plate_barcode = Column(String)
    aliquot_well_id = Column(String)
    aliquot_vial_barcode = Column(String)
    aliquot_amount =Column(DECIMAL)
    aliquot_amount_unit = Column(String)
    sample_appearance = Column(String)
    structure_name = Column(String)
    cas_regno = Column(String)
    supplier_sample_id = Column(String)
    aliquot_date = Column(String)
    solubilized_barcode = Column(String)
    lts_barcode = Column(String)
    source_barcode = Column(String)
    purity =Column(DECIMAL)
    purity_method = Column(String)
    bottle_id = Column(Integer)
    shipment_file_id = Column(Integer)
    blinded_sample_id = Column(String)
    legacy_id = Column(String)
    mapped_other = Column(Integer, default=0)
    aliquot_conc = Column(FLOAT)
    aliquot_conc_unit = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)