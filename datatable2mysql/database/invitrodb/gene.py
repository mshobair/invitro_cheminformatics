import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class Gene(Base):
    """Maps to Gene table in invitrodb databases."""

    __tablename__ = 'gene'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    gene_id = Column(Integer, nullable=False, primary_key=True)
    entrez_gene_id = Column(Integer)
    official_full_name = Column(String(255))
    gene_name = Column(String(255))
    official_symbol = Column(String(32))
    gene_symbol = Column(String(32))
    description = Column(String(255))
    uniprot_accession_number = Column(String(32))
    organism_id = Column(Integer)
    track_status = Column(String(32))