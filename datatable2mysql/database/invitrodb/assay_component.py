import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import TEXT


from database.base import Base


class AssayComponent(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_component'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    acid = Column(Integer, nullable=False, primary_key=True)
    aid = Column(Integer, nullable=False)
    assay_component_name = Column(String(255), nullable=False)
    assay_component_desc = Column(TEXT)
    assay_component_target_desc = Column(TEXT)
    parameter_readout_type = Column(String(255))
    assay_design_type = Column(String(255))
    assay_design_type_sub = Column(String(255))
    biological_process_target = Column(String(255))
    detection_technology_type = Column(String(255))
    detection_technology_type_sub = Column(String(255))
    detection_technology = Column(String(255))
    signal_direction_type = Column(String(255))
    key_assay_reagent_type = Column(String(255))
    key_assay_reagent = Column(String(255))
    technological_target_type = Column(String(255))
    technological_target_type_sub = Column(String(255))
