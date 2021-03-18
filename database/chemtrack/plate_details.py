import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, Float

from database.base import Base


class PlateDetails(Base):
    """Maps to plate_details table in chemprop databases."""

    __tablename__ = 'plate_details'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    ism = Column(String)
    sample_id = Column(String)
    structure_id = Column(String)
    structure_real_amw = Column(String)
    sample_supplier = Column(String)
    supplier_structure_id = Column(String)
    aliquot_plate_barcode = Column(String)
    aliquot_well_id = Column(String)
    aliquot_solvent = Column(String)
    aliquot_conc = Column(Float)
    aliquot_conc_unit = Column(String)
    aliquot_volume = Column(Integer)
    aliquot_volume_unit = Column(String)
    sample_appearance = Column(String)
    structure_name = Column(String)
    cas_regno = Column(String)
    supplier_sample_id = Column(String)
    aliquot_date = Column(String)
    solubilized_barcode = Column(String)
    lts_barcode = Column(String)
    bottle_id = Column(Integer)
    shipment_file_id = Column(Integer)
    blinded_sample_id = Column(String)
    plate_id = Column(Integer)
    legacy_id = Column(String)
    legacy_sample = Column(String)
    legacy_sample_id = Column(String)
    mapped_other = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)