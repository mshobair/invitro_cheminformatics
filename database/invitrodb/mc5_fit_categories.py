import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc5FitCategories(Base):
    """Maps to mc5_fit_categories table in invitrodb databases."""

    __tablename__ = 'mc5_fit_categories'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    fitc = Column(Integer, nullable=False)
    parent_fitc = Column(Integer)
    name = Column(String(30), nullable=False)
    xloc = Column(DOUBLE, nullable=False)
    yloc = Column(DOUBLE, nullable=False)