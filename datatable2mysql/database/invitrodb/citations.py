import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import MEDIUMTEXT, LONGTEXT


from database.base import Base


class Citations(Base):
    """Maps to citations table in invitrodb databases."""

    __tablename__ = 'citations'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    citation_id = Column(Integer, nullable=False, primary_key=True)
    pmid = Column(Integer)
    doi = Column(MEDIUMTEXT)
    other_source = Column(MEDIUMTEXT)
    other_id = Column(MEDIUMTEXT)
    citation = Column(LONGTEXT, nullable=False)
    title = Column(LONGTEXT)
    author = Column(LONGTEXT)
    url = Column(LONGTEXT)