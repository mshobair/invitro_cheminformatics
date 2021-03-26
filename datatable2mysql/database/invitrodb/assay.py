import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import DOUBLE, TEXT


from database.base import Base

class Assay(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__= 'assay'
    __table_args__= {'schema': Schemas.invitrodb_schema}

    aid = Column(Integer, primary_key=True, nullable=False)
    asid = Column(Integer, nullable=False)
    assay_name = Column(String(255), nullable=False)
    assay_desc = Column(TEXT)
    timepoint_hr = Column(DOUBLE)
    organism_id = Column(Integer)
    organism = Column(String(255))
    tissue = Column(String(255))
    cell_format = Column(String(255))
    cell_free_component_source = Column(String(255))
    cell_short_name = Column(String(255))
    cell_growth_mode = Column(String(255))
    assay_footprint = Column(String(255))
    assay_format_type = Column(String(255))
    assay_format_type_sub = Column(String(255))
    content_readout_type = Column(String(255))
    dilution_solvent = Column(String(255))
    dilution_solvent_percent_max = Column(String(255))