import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class Mc3Aeid(Base):
    """Maps to mc3_aeid table in invitrodb databases."""

    __tablename__ = 'mc3_aeid'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    mc3_mthd_id = Column(Integer, nullable=False, primary_key=True)
    aeid = Column(Integer, nullable=False, primary_key=True)
    exec_ordr = Column(Integer, nullable=False, default=1)

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)