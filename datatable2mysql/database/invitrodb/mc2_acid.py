import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


from database.base import Base


class Mc2Acid(Base):
    """Maps to mc2_acid table in invitrodb databases."""

    __tablename__ = 'mc2_acid'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    mc2_mthd_id = Column(Integer, nullable=False, primary_key=True)
    acid = Column(Integer, nullable=False, primary_key=True)
    exec_ordr = Column(Integer, nullable=False, default=1)

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)