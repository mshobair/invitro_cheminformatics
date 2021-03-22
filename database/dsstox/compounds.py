import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import DOUBLE, BLOB

from database.base import Base


class Compounds(Base):
    """Maps to compounds table in dsstox databases."""

    __tablename__ = 'compounds'
    __table_args__ = {'schema': Schemas.dsstox_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    dsstox_compound_id = Column(String(255))
    chiral_stereo = Column(String(255))
    double_stereo = Column(String(255))
    chemical_type = Column(String(255))
    organic_form = Column(String(255))
    mrv_file = Column(String, nullable=False)
    mol_file = Column(String)
    mol_file_3d = Column(String)
    smiles = Column(String)
    inchi = Column(String)
    jchem_inchi_key = Column(String(255))
    indigo_inchi_key = Column(String(255))
    acd_iupac_name = Column(String(5000))
    acd_index_name = Column(String(5000))
    pubchem_iupac_name = Column(String(5000))
    mol_formula = Column(String(255))
    mol_weight = Column(DOUBLE)
    monoisotopic_mass = Column(DOUBLE)
    fragment_count = Column(Integer)
    has_defined_isotope = Column(Integer)
    radical_count = Column(Integer)
    pubchem_cid = Column(Integer)
    chemspider_id = Column(Integer)
    chebi_id = Column(Integer)
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    mol_image_png = Column(BLOB)
    has_stereochemistry = Column(Integer)
    pubchem_sources = Column(Integer)
