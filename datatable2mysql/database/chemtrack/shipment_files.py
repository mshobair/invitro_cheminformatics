import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class ShipmentFiles(Base):
    """Maps to shipment_files table in chemprop databases."""

    __tablename__ = 'shipment_files'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    filename = Column(String)
    file_url = Column(String)
    file_kilobytes = Column(Integer)
    comment = Column(String)
    vendor_id = Column(Integer)
    order_number = Column(String)
    evotech_order_num = Column(String)
    evotech_shipment_num = Column(String)
    original_filename = Column(String)
    chemical_set = Column(String)
    e_ship_num_change = Column(String)
    target_conc_mm = Column(Integer)
    shipped_date_depr = Column(Integer)
    asid = Column(Integer)
    asnm = Column(String)
    use_disposition = Column(String)
    plate_set_count = Column(Integer)
    plate_set = Column(Integer)
    solvent = Column(String)
    aliquot_date = Column(String)
    legacy_date_added = Column(Integer)
    ship_id = Column(String)
    vial = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    task_order_id = Column(Integer)
    address_id = Column(Integer)
    order_concentration_id = Column(Integer)
    external = Column(Integer, default=0)
    plate_detail = Column(String)
    amount = Column(Integer)
    status = Column(String)
    amount_unit = Column(String)
    order_id = Column(Integer)
    mixture = Column(Integer, default=0)
    shipped_date = Column(DateTime)