import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Organism(Base):
    """Maps to organism table in invitrodb databases."""

    __tablename__ = 'organism'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    organism_id = Column(Integer, nullable=False, primary_key=True)
    ncbi_taxon_id = Column(Integer)
    taxon_name = Column(String(255))
    common_name = Column(String(255))
    lineage = Column(String(255))