import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Tox21Chemicals(Base):
    """Maps to tox_21_chemicals table in chemprop databases."""

    __tablename__ = 'tox_21_chemicals'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    t_tox21_id = Column(String)
    t_original_sample_id = Column(String)
    t_partner = Column(String)
    t_tox21_ntp_sid = Column(String)
    t_tox21_ncgc_id = Column(String)
    t_pubchem_regid = Column(String)
    t_pubchem_sid = Column(Integer)
    t_pubchem_cid = Column(Integer)
    t_pubchem_name = Column(String)
    t_pubchem_cas = Column(String)
    t_qc_grade_id = Column(String)