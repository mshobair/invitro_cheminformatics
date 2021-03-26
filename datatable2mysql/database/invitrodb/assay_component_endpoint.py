import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import TEXT, TINYINT


from database.base import Base


class AssayComponentEndpoint(Base):
    """Maps to assay table in invitrodb databases."""

    __tablename__ = 'assay_component_endpoint'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    aeid = Column(Integer, nullable=False, primary_key=True)
    acid = Column(Integer, nullable=False)
    assay_component_endpoint_name = Column(String(255), nullable=False)
    export_ready = Column(TINYINT, nullable=False)
    internal_ready = Column(TINYINT)
    assay_component_endpoint_desc = Column(TEXT)
    assay_function_type = Column(String(255))
    normalized_data_type = Column(String(255))
    analysis_direction = Column(String(255))
    burst_assay = Column(TINYINT, nullable=False)
    key_positive_control = Column(String(255))
    signal_direction = Column(String(255))
    intended_target_type = Column(String(255))
    intended_target_type_sub = Column(String(255))
    intended_target_family = Column(String(255))
    intended_target_family_sub = Column(String(255))
    fit_all = Column(TINYINT, nullable=False)
