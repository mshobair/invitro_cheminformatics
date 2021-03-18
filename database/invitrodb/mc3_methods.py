import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base

class Mc3Methods(Base):
    """Maps to mc3_methods table in invitrodb databases."""

    __tablename__= 'mc3_methods'
    __table_args__= {'schema': Schemas.invitrodb_schema}

    mc3_mthd_id = Column(Integer, nullable=False, primary_key=True)
    mc3_mthd = Column(String(50), nullable=False)
    desc = Column(String(255))

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)