import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sc1Methods(Base):
    """Maps to sc1_methods table in invitrodb databases."""

    __tablename__ = 'sc1_methods'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    sc1_mthd_id = Column(Integer, nullable=False, primary_key=True)
    sc1_mthd = Column(String(50), nullable=False)
    desc = Column(String(255))

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)